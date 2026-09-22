// ── Chat Panel (REST + SSE connected to Houdini) ──

import { addOrbMessage } from './orb-messages.js';
import { updateSystemData } from './system-monitor.js';
import { getConfig } from '../config/config-loader.js';
import { renderMarkdown } from './markdown.js';

const terminalContent = document.getElementById('terminal-content');
const chatInput = document.getElementById('chat-input');
const chatSend = document.getElementById('chat-send');

// Model Status 面板 DOM
const modelNameEl = document.getElementById('model-name');
const tokensInEl = document.getElementById('tokens-in');
const tokensOutEl = document.getElementById('tokens-out');
const contextValueEl = document.getElementById('context-value');
const contextBarEl = document.getElementById('context-bar');
const contextBarLabelEl = document.getElementById('context-bar-label');
// 單次對話 token 使用量
let lastTokensIn = 0;
let lastTokensOut = 0;
let contextWindow = 128000;  // 會從 API 更新

// ── 里程表數字滾動效果 ──

const isMobileView = window.matchMedia('(max-width: 768px)').matches;

function createOdometer(el) {
  if (!el || el.dataset.odometer === 'ready') return;
  el.dataset.odometer = 'ready';
  el.style.cssText += `
    display: inline-flex;
    overflow: hidden;
    height: 1.2em;
    line-height: 1.2em;
    vertical-align: bottom;
  `;
}

function setOdometerValue(el, value, duration = 800) {
  if (!el) return;

  // 手機版直接顯示文字（odometer 排版會壞）
  if (isMobileView) {
    const formatted = typeof value === 'string' ? value : value.toLocaleString();
    el.textContent = formatted;
    return;
  }

  createOdometer(el);

  const formatted = typeof value === 'string' ? value : value.toLocaleString();
  const chars = formatted.split('');

  // 第一次使用時清空原始文字內容
  if (!el.querySelector('.odo-col')) {
    el.textContent = '';
  }

  // 確保有足夠的 columns（移除多餘的）
  while (el.children.length > chars.length) {
    el.removeChild(el.lastChild);
  }

  chars.forEach((char, i) => {
    let col = el.children[i];

    if (!col) {
      col = document.createElement('span');
      col.className = 'odo-col';
      el.appendChild(col);
    }

    // 非數字字元（逗號、%）直接顯示
    if (!/\d/.test(char)) {
      col.style.cssText = `
        display: inline-block;
        width: auto;
        height: 1.2em;
        line-height: 1.2em;
        overflow: hidden;
      `;
      col.innerHTML = '';
      col.textContent = char;
      col.className = 'odo-col odo-sep';
      return;
    }

    const digit = parseInt(char);
    col.className = 'odo-col';
    col.style.cssText = `
      display: inline-block;
      width: 0.65em;
      height: 1.2em;
      overflow: hidden;
      position: relative;
      text-align: center;
    `;

    // 建立數字捲軸（0-9 + 再一個 0 用於循環）
    let strip = col.querySelector('.odo-strip');
    if (!strip) {
      strip = document.createElement('span');
      strip.className = 'odo-strip';
      strip.style.cssText = `
        display: block;
        transition: transform ${duration}ms cubic-bezier(0.23, 1, 0.32, 1);
        will-change: transform;
      `;
      strip.innerHTML = '0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9';
      col.innerHTML = '';
      col.appendChild(strip);
    }

    // 更新動畫時長
    strip.style.transitionDuration = duration + 'ms';

    // 滾動到目標數字
    requestAnimationFrame(() => {
      strip.style.transform = `translateY(-${digit * 1.2}em)`;
    });
  });
}

// 進度條平滑動畫
function animateBar(barEl, toPct, duration = 800) {
  if (!barEl) return;
  barEl.style.transition = `width ${duration}ms cubic-bezier(0.23, 1, 0.32, 1)`;
  barEl.style.width = toPct + '%';
}

// 從後端拉 Model Status
async function fetchModelStatus() {
  try {
    const res = await fetch('/api/model-status');
    if (!res.ok) return;
    const data = await res.json();

    // 模型名稱
    if (data.model && modelNameEl) {
      const display = data.provider
        ? `${data.provider}/${data.model}`.toUpperCase()
        : data.model.toUpperCase();
      modelNameEl.textContent = display;
    }
    if (data.contextWindow) contextWindow = data.contextWindow;

    // Token 使用量（單次對話的 input / output）
    if (data.usage) {
      lastTokensIn = data.usage.input || 0;
      lastTokensOut = data.usage.output || 0;
    }
    setOdometerValue(tokensInEl, lastTokensIn);
    setOdometerValue(tokensOutEl, lastTokensOut);

    // Context 使用率
    const total = data.totalTokens || (lastTokensIn + lastTokensOut);
    const pct = Math.min(100, Math.round((total / contextWindow) * 100));
    setOdometerValue(contextValueEl, pct + '%');
    animateBar(contextBarEl, pct);
    if (contextBarLabelEl) contextBarLabelEl.textContent = pct + '%';
  } catch {
    // ignore
  }
}

let isWaiting = false;
let currentReplyLine = null;
let replyBuffer = '';
let activeRunId = null;  // 追蹤我們送出的 runId

// TTS 語音播放（透過事件通知 audio.js → Orb + 頻譜 + 波形連動）
let ttsEnabled = true;

async function speakText(text) {
  if (!ttsEnabled || !text) return;
  
  // Pausar micrófono mientras habla Houdini (evita feedback)
  const wasListening = isListening;
  if (wasListening && window.__toggleListening) {
    window.__toggleListening();
  }
  
  try {
    // Limpiar markdown para mejor TTS
    const cleanText = text
      .replace(/\*\*(.*?)\*\*/g, '$1')
      .replace(/\*(.*?)\*/g, '$1')
      .replace(/```[\s\S]*?```/g, '')
      .replace(/`([^`]+)`/g, '$1')
      .replace(/^#{1,6}\s+/gm, '')
      .replace(/\n{3,}/g, '\n')
      .trim();

    // Dividir en fragmentos de 800 chars
    const MAX_CHUNK = 800;
    const chunks = [];
    for (let i = 0; i < cleanText.length; i += MAX_CHUNK) {
      chunks.push(cleanText.slice(i, i + MAX_CHUNK));
    }

    for (let i = 0; i < chunks.length; i++) {
      const res = await fetch('/api/tts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: chunks[i] }),
      });
      if (!res.ok) continue;

      const blob = await res.blob();
            const url = URL.createObjectURL(blob);

            // Reproducir con el elemento de audio existente en la página
      let audioEl = document.getElementById('houdini-tts-player');
            if (!audioEl) {
              audioEl = document.createElement('audio');
              audioEl.id = 'houdini-tts-player';
              audioEl.style.display = 'none';
              document.getElementById('audio-controls')?.appendChild(audioEl) || document.body.appendChild(audioEl);
            }
            audioEl.src = url;
            await new Promise((resolve) => {
              audioEl.onended = () => { URL.revokeObjectURL(url); resolve(); };
              audioEl.onerror = () => { URL.revokeObjectURL(url); resolve(); };
              audioEl.play().catch(() => { URL.revokeObjectURL(url); resolve(); });
            });
    }
    
    // Reactivar micrófono si estaba activo antes de hablar
    if (wasListening && window.__toggleListening && !isListening) {
      window.__toggleListening();
    }
  } catch {
    // TTS falla silenciosamente
  }
}

// 串流速度追蹤
let lastStreamLen = 0;
let lastStreamTime = 0;
let streamSpeedTimer = null;

// ── SSE 串流 ──
// ── 載入 Gateway 歷史訊息 ──
async function loadHistory() {
  try {
    const displayLimit = parseInt(localStorage.getItem('jarvis-history-limit') || '50');
    // 多拉幾倍，因為 tool calls/heartbeat 會被過濾掉
    const fetchLimit = displayLimit * 4;
    const res = await fetch(`/api/history?limit=${fetchLimit}`);
    if (!res.ok) return;
    const data = await res.json();
    const messages = data.messages || [];

    // 過濾出 user/assistant 的文字訊息
    const chatMessages = [];
    for (const m of messages) {
      if (m.role !== 'user' && m.role !== 'assistant') continue;
      // 跳過包含 tool call 的 assistant 訊息（純工具呼叫不是對話）
      const hasToolCall = (m.content || []).some(c => c.type === 'toolCall');
      const texts = (m.content || [])
        .filter(c => c.type === 'text' && c.text?.trim())
        .map(c => {
          let t = c.text.trim();
          // 剝離 Conversation info metadata，保留使用者實際文字
          if (t.startsWith('Conversation info')) {
            const parts = t.split('\n```\n\n');
            t = parts.length > 1 ? parts.slice(1).join('\n```\n\n').trim() : '';
          }
          return t;
        })
        .filter(t => t && !t.startsWith('Read HEARTBEAT'))
        .filter(t => t !== 'HEARTBEAT_OK')
        .filter(t => t !== 'NO_REPLY')
        .filter(t => !t.startsWith('System:'))
        .filter(t => !t.startsWith('Pre-compaction'));
      if (!texts.length) continue;
      // assistant 有 tool call 但也有文字 → 保留文字（最終回覆）
      // assistant 只有 tool call → 跳過
      if (m.role === 'assistant' && hasToolCall && !m.stopReason?.includes('end_turn')) continue;
      chatMessages.push({
        role: m.role,
        text: texts.join('\n'),
        timestamp: m.timestamp,
      });
    }

    if (!chatMessages.length) return;

    // 只取最後 N 則實際對話
    const displayMessages = chatMessages.slice(-displayLimit);

    // 加一條分隔線
    addChatLine(`── HISTORIAL (${displayMessages.length}) ──`, 'system-line');

    for (const msg of displayMessages) {
      const className = msg.role === 'user' ? 'user-line' : 'jin-line';
      const line = addChatLine('', className);
      if (!line) continue;

      // 用時間戳覆蓋 timeStamp()
      if (msg.timestamp) {
        const timeEl = line.querySelector('.msg-time');
        if (timeEl) {
          const d = new Date(msg.timestamp);
          const hh = String(d.getHours()).padStart(2, '0');
          const mm = String(d.getMinutes()).padStart(2, '0');
          timeEl.textContent = `${d.getMonth() + 1}/${d.getDate()} ${hh}:${mm}`;
        }
      }

      // 渲染文字（assistant 用 markdown）
      const msgText = line.querySelector('.msg-text');
      if (msgText) {
        if (msg.role === 'assistant') {
          msgText.innerHTML = renderMarkdown(msg.text);
        } else {
          msgText.textContent = msg.text;
        }
      }
    }

    addChatLine('── FIN HISTORIAL ──', 'system-line');
    if (terminalContent) terminalContent.scrollTop = terminalContent.scrollHeight;
  } catch {
    // 靜默失敗，不影響正常使用
  }
}

function connectSSE() {
  const evtSource = new EventSource('/api/events');
  window.__jarvisSSE = evtSource;  // 共用給 tasks.js, schedule.js 等

  evtSource.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);

      if (data.type === 'connected') {
        addChatLine('FLUJO GATEWAY CONECTADO ✓', 'system-line');
        return;
      }

      if (data.type === 'system') {
        updateSystemData(data);
        return;
      }

      // chat 事件串流
      handleChatEvent(data);
    } catch {
      // ignore
    }
  };

  evtSource.onerror = () => {
    // SSE 自動重連
  };
}

function handleChatEvent(data) {
  const text = data.text || '';
  const done = data.done || false;

  // ── Mensajes del asistente de escritorio (mostrar sin repetir TTS) ──
    if (data.state === 'from_assistant' && data.text_user) {
      // Mostrar mensaje del usuario
      addChatLine(data.text_user, 'user-line');
      // Mostrar respuesta del asistente sin TTS
      addChatLine(data.text, 'jin-line');
      window.dispatchEvent(new CustomEvent('agent-state', { detail: 'idle' }));
      return;
    }

  // 只處理我們送出的 runId，或是沒指定 runId 的通用事件
  if (data.runId && activeRunId && data.runId !== activeRunId) return;

  // 有文字 → 更新回覆行
  if (text) {
    if (!currentReplyLine) {
      currentReplyLine = addChatLine('', 'jin-line');
      replyBuffer = '';
      lastStreamLen = 0;
      lastStreamTime = performance.now();
      window.dispatchEvent(new CustomEvent('agent-state', { detail: 'responding' }));

      // 定期計算串流速度
      if (streamSpeedTimer) clearInterval(streamSpeedTimer);
      streamSpeedTimer = setInterval(() => {
        const now = performance.now();
        const dt = (now - lastStreamTime) / 1000;
        if (dt > 0) {
          const charsPerSec = (replyBuffer.length - lastStreamLen) / dt;
          // 正規化：~50 chars/sec = 1.0 強度
          const intensity = Math.min(1, charsPerSec / 50);
          window.dispatchEvent(new CustomEvent('agent-stream', { detail: intensity }));
          lastStreamLen = replyBuffer.length;
          lastStreamTime = now;
        }
      }, 200);
    }
    // delta 是累積的完整文字
    replyBuffer = text;
    if (currentReplyLine) {
      const msgSpan = currentReplyLine.querySelector('.msg-text');
      if (msgSpan) msgSpan.textContent = replyBuffer;
      terminalContent.scrollTop = terminalContent.scrollHeight;
    }
  }

  if (done) {
    // 清理串流追蹤
    if (streamSpeedTimer) { clearInterval(streamSpeedTimer); streamSpeedTimer = null; }
    window.dispatchEvent(new CustomEvent('agent-stream', { detail: 0 }));

    // 回覆完成 → 更新 Model Status（streaming 不帶 usage，需另外拉）
    fetchModelStatus();

    // 回覆完成 → Orb 通知
    if (replyBuffer) {
          const cfg = getConfig();
          const agentName = cfg?.agent?.name || 'JARVIS';
          // Sin texto flotante en el orbe (solo voz)
          // addOrbMessage(`${agentName}: ${replyBuffer}`);
          // No reproducir TTS aquí — ya lo hace handleChatSend

      // 串流完成 → Markdown 渲染
      if (currentReplyLine) {
        const msgBody = currentReplyLine.querySelector('.msg-body');
        if (msgBody) {
          const timeEl = msgBody.querySelector('.msg-time');
          msgBody.innerHTML = renderMarkdown(replyBuffer);
          if (timeEl) msgBody.appendChild(timeEl);
        }
        currentReplyLine.classList.add('markdown-rendered');
        terminalContent.scrollTop = terminalContent.scrollHeight;
      }
    }
    currentReplyLine = null;
    replyBuffer = '';
    activeRunId = null;
    isWaiting = false;
    window.dispatchEvent(new CustomEvent('agent-state', { detail: 'idle' }));
    if (chatSend) chatSend.textContent = 'ENVIAR';
  }
}

// 時間戳格式
function timeStamp() {
  const now = new Date();
  return now.toLocaleTimeString('es', { hour: '2-digit', minute: '2-digit' });
}

// ── 公開 API ──
export function addChatLine(text, className, images = []) {
  if (!terminalContent) return null;

  const line = document.createElement('div');
  line.className = `terminal-line ${className}`;

  // 系統訊息不加時間戳和標籤
  if (className.includes('system-line') || className.includes('command-line')) {
    line.textContent = text;
  } else {
    // 發送者標籤
    const sender = document.createElement('span');
    sender.className = 'msg-sender';
    const cfg = getConfig();
    sender.textContent = className.includes('user-line') ? 'TÚ' : (cfg?.agent?.name || 'HOUDINI').toUpperCase();
    line.appendChild(sender);

    // 內容行（text + time）
    const msgBody = document.createElement('div');
    msgBody.className = 'msg-body';

    // 圖片預覽
    if (images.length) {
      const imgContainer = document.createElement('div');
      imgContainer.className = 'msg-images';
      images.forEach(src => {
        const img = document.createElement('img');
        img.src = src;
        img.className = 'msg-image';
        img.addEventListener('click', () => window.open(src, '_blank'));
        imgContainer.appendChild(img);
      });
      msgBody.appendChild(imgContainer);
    }

    const msgText = document.createElement('span');
    msgText.className = 'msg-text';
    msgText.textContent = text;
    msgBody.appendChild(msgText);

    const time = document.createElement('span');
    time.className = 'msg-time';
    time.textContent = timeStamp();
    msgBody.appendChild(time);

    line.appendChild(msgBody);
  }

  terminalContent.appendChild(line);

  // 限制 terminal 行數，避免 DOM 無限膨脹
  const MAX_LINES = 100;
  const lines = terminalContent.querySelectorAll('.terminal-line');
  if (lines.length > MAX_LINES) {
    const excess = lines.length - MAX_LINES;
    for (let i = 0; i < excess; i++) lines[i].remove();
  }

  terminalContent.scrollTop = terminalContent.scrollHeight;
  return line;
}

export function addTerminalMessage(message, isCommand = false) {
  if (!terminalContent) return;
  const newLine = document.createElement('div');
  newLine.className = isCommand ? 'terminal-line command-line' : 'terminal-line system-line';
  newLine.textContent = message;
  terminalContent.appendChild(newLine);
  terminalContent.scrollTop = terminalContent.scrollHeight;
}

// ── 送出 ──
const chatAttach = document.getElementById('chat-attach');
const chatFileInput = document.getElementById('chat-file-input');
let pendingFiles = [];  // 待發送的附件

const ATTACH_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.44 11.05l-9.19 9.19a6 6 0 01-8.49-8.49l9.19-9.19a4 4 0 015.66 5.66l-9.2 9.19a2 2 0 01-2.83-2.83l8.49-8.48"/></svg>';

function updateAttachBtn(count) {
  if (!chatAttach) return;
  chatAttach.classList.toggle('has-files', count > 0);
  chatAttach.innerHTML = count > 0 ? `${ATTACH_SVG}<span class="attach-badge">${count}</span>` : ATTACH_SVG;
}

// 附件按鈕
if (chatAttach && chatFileInput) {
  chatAttach.addEventListener('click', () => chatFileInput.click());
  chatFileInput.addEventListener('change', () => {
    pendingFiles = Array.from(chatFileInput.files || []);
    updateAttachBtn(pendingFiles.length);
  });
}

// Orb 拖放
const orbDropZone = document.getElementById('three-container') || document.body;
['dragenter', 'dragover'].forEach(evt => {
  orbDropZone.addEventListener(evt, (e) => {
    e.preventDefault();
    e.stopPropagation();
    orbDropZone.classList.add('drag-over');
  });
});
['dragleave', 'drop'].forEach(evt => {
  orbDropZone.addEventListener(evt, (e) => {
    e.preventDefault();
    e.stopPropagation();
    orbDropZone.classList.remove('drag-over');
  });
});
orbDropZone.addEventListener('drop', (e) => {
  const files = Array.from(e.dataTransfer?.files || []);
  if (!files.length) return;
  pendingFiles = files;
  updateAttachBtn(files.length);
  // 自動送出：分析這些檔案
  chatInput.value = chatInput.value || 'Analiza estos archivos';
  handleChatSend();
});

// ── Session ID persistente (localStorage) ──
function getSessionId() {
  let sid = localStorage.getItem('houdini-session-id');
  if (!sid) {
    sid = 'houdini-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 8);
    localStorage.setItem('houdini-session-id', sid);
  }
  return sid;
}

async function handleChatSend() {
  if (!chatInput || isWaiting) return;
  const msg = chatInput.value.trim();
  const hasFiles = pendingFiles.length > 0;
  if (!msg && !hasFiles) return;

  // 用戶互動時提前初始化 AudioContext（解決手機 autoplay 限制）
  window.dispatchEvent(new Event('user-interaction'));

  // 顯示附件資訊（含圖片預覽）
  if (hasFiles) {
    const imageUrls = [];
    const fileNames = [];
    pendingFiles.forEach(f => {
      fileNames.push(f.name);
      if (f.type.startsWith('image/')) {
        imageUrls.push(URL.createObjectURL(f));
      }
    });
    addChatLine(msg || `📎 ${fileNames.join(', ')}`, 'user-line', imageUrls);
  } else {
    addChatLine(msg, 'user-line');
  }
  chatInput.value = '';

  isWaiting = true;
  window.dispatchEvent(new CustomEvent('agent-state', { detail: 'thinking' }));
  if (chatSend) chatSend.textContent = '...';

  // 不預建回覆行，等 SSE 第一個 chunk 再建
  currentReplyLine = null;
  replyBuffer = '';

  try {
    let res;
    if (hasFiles) {
      // 帶檔案 → FormData
      const formData = new FormData();
      formData.append('message', msg);
      pendingFiles.forEach(f => formData.append('files', f));
      res = await fetch('/api/chat/upload', { method: 'POST', body: formData });
      // 清除附件
      pendingFiles = [];
      if (chatAttach) { updateAttachBtn(0); }
      if (chatFileInput) chatFileInput.value = '';
    } else {
      res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg, session_id: getSessionId() }),
      });
    }

    const result = await res.json();

    if (!res.ok) {
      addChatLine(`ERROR: ${result.error || 'Error desconocido'}`, 'system-line');
      currentReplyLine = null;
      activeRunId = null;
      isWaiting = false;
      window.dispatchEvent(new CustomEvent('agent-state', { detail: 'idle' }));
      if (chatSend) chatSend.textContent = 'ENVIAR';
      return;
    }

    // ── Respuesta directa desde Houdini Bridge ──
    if (result.text) {
      // Crear línea de respuesta
      const cfg = getConfig();
      const agentName = cfg?.agent?.name || 'HOUDINI';
      addChatLine(result.text, 'jin-line');

      // TTS automático
      speakText(result.text);

      // Agregar mensaje al orb (breve, solo notificación)
            // No se muestran textos flotantes alrededor del orbe

      // Estado idle
            window.dispatchEvent(new CustomEvent('agent-state', { detail: 'idle' }));
            if (chatSend) chatSend.textContent = 'ENVIAR';
            isWaiting = false;

            // ── Preguntar si quiere guardar datos detectados ──
            if (result.pending_save && Object.keys(result.pending_save).length > 0) {
              const labels = { name: '📝 nombre', telegram_chat_id: '💬 Chat ID de Telegram' };
              const parts = [];
              for (const [key, val] of Object.entries(result.pending_save)) {
                parts.push(`${labels[key] || key}: ${val}`);
              }
              setTimeout(() => {
                addChatLine(`💾 He detectado estos datos: ${parts.join(', ')}. ¿Deseas guardarlos para no tener que repetirlos?`, 'system-line');
                // Botones de confirmación
                const line = addChatLine('', 'system-line');
                if (line) {
                  const btnContainer = document.createElement('div');
                  btnContainer.style.cssText = 'display:flex;gap:8px;margin-top:4px';
            
                  const saveBtn = document.createElement('button');
                  saveBtn.textContent = '✅ GUARDAR';
                  saveBtn.className = 'btn';
                  saveBtn.style.cssText = 'padding:4px 12px;font-size:11px;border:1px solid var(--accent-primary);background:rgba(var(--accent-rgb),0.15);color:var(--accent-primary);cursor:pointer;border-radius:4px';
                  saveBtn.addEventListener('click', async () => {
                    try {
                      const r = await fetch('/api/profile/save', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ data: result.pending_save }),
                      });
                      const d = await r.json();
                      if (d.ok) addChatLine('✅ Datos guardados permanentemente.', 'system-line');
                    } catch {}
                  });
            
                  const noBtn = document.createElement('button');
                  noBtn.textContent = '❌ NO GUARDAR';
                  noBtn.className = 'btn';
                  noBtn.style.cssText = 'padding:4px 12px;font-size:11px;border:1px solid #666;background:transparent;color:#999;cursor:pointer;border-radius:4px';
                  noBtn.addEventListener('click', () => {
                    addChatLine(' Entendido, no guardo nada.', 'system-line');
                  });
            
                  btnContainer.appendChild(saveBtn);
                  btnContainer.appendChild(noBtn);
                  line.appendChild(btnContainer);
                }
              }, 500);
            }
      activeRunId = null;

      // Actualizar model status
      fetchModelStatus();
      return;
    }

    // Legacy: 記錄 runId，等 SSE 串流
    activeRunId = result.runId || null;

    // 超時 fallback
    setTimeout(() => {
      if (isWaiting && activeRunId === result.runId) {
        if (!replyBuffer) {
          addChatLine('TIMEOUT — TIEMPO AGOTADO', 'system-line');
        }
        if (streamSpeedTimer) { clearInterval(streamSpeedTimer); streamSpeedTimer = null; }
        window.dispatchEvent(new CustomEvent('agent-stream', { detail: 0 }));
        currentReplyLine = null;
        activeRunId = null;
        isWaiting = false;
        window.dispatchEvent(new CustomEvent('agent-state', { detail: 'idle' }));
        if (chatSend) chatSend.textContent = 'ENVIAR';
      }
    }, 60000);

  } catch (err) {
    addChatLine(`CONNECTION ERROR: ${err.message}`, 'system-line');
    if (streamSpeedTimer) { clearInterval(streamSpeedTimer); streamSpeedTimer = null; }
    window.dispatchEvent(new CustomEvent('agent-stream', { detail: 0 }));
    currentReplyLine = null;
    isWaiting = false;
    window.dispatchEvent(new CustomEvent('agent-state', { detail: 'idle' }));
    if (chatSend) chatSend.textContent = 'ENVIAR';
  }
  
}

// ── Voice Input — Always Listening (Jarvis Mode) ──
let recognition = null;
let isListening = false;
let silenceTimer = null;
let lastTranscript = '';
const micBtn = document.getElementById('chat-mic');
let vadTimeout = null;

function initVoiceInput() {
  if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
    if (micBtn) micBtn.style.display = 'none';
    return;
  }

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  
  function createRecognizer() {
    const rec = new SpeechRecognition();
    rec.lang = 'es-CO';
    rec.continuous = true;
    rec.interimResults = true;
    rec.maxAlternatives = 1;
    return rec;
  }

  function handleResult(event) {
    let finalText = '';
    let interimText = '';
    
    for (let i = event.resultIndex; i < event.results.length; i++) {
      const result = event.results[i];
      if (result.isFinal) {
        finalText += result[0].transcript;
      } else {
        interimText += result[0].transcript;
      }
    }
    
    const displayText = (finalText + ' ' + interimText).trim();
    if (displayText && chatInput) {
      chatInput.value = displayText;
      chatInput.placeholder = '🎤 ESCUCHANDO...';
    }
    
    lastTranscript = finalText;
    
    if (silenceTimer) clearTimeout(silenceTimer);
    
    if (finalText.trim()) {
      silenceTimer = setTimeout(() => {
        if (chatInput && chatInput.value.trim()) {
          chatInput.placeholder = '🎤 Procesando...';
          handleChatSend();
        }
      }, 1800);
    }
  }

  function startListening() {
    if (isListening) return;
    isListening = true;
    
    recognition = createRecognizer();
    
    recognition.onresult = handleResult;
    
    recognition.onend = function() {
      if (!isListening) return;
      try {
        const rec = createRecognizer();
        rec.onresult = handleResult;
        rec.onend = arguments.callee;
        rec.onerror = function(e) {
          if (!isListening) return;
          setTimeout(startListening, 500);
        };
        rec.start();
        recognition = rec;
      } catch(e) {
        if (isListening) setTimeout(startListening, 1000);
      }
    };
    
    recognition.onerror = function(event) {
      if (event.error === 'not-allowed') {
        isListening = false;
        if (micBtn) micBtn.style.display = 'none';
        return;
      }
      if (isListening) {
        setTimeout(startListening, 500);
      }
    };
    
    try {
      recognition.start();
      if (micBtn) micBtn.classList.add('recording');
      if (chatInput) chatInput.placeholder = '🎤 Siempre escuchando...';
    } catch(e) {
      isListening = false;
      setTimeout(startListening, 1000);
    }
  }

  function stopListening() {
    isListening = false;
    if (recognition) {
      try { recognition.stop(); } catch(e) {}
    }
    if (silenceTimer) clearTimeout(silenceTimer);
    if (micBtn) micBtn.classList.remove('recording');
    if (chatInput) chatInput.placeholder = 'ESCRIBE UN MENSAJE...';
  }

  window.__toggleListening = function() {
    if (isListening) {
      stopListening();
      if (micBtn) micBtn.title = 'ACTIVAR VOZ';
    } else {
      startListening();
      if (micBtn) micBtn.title = 'MODO SIEMPRE ACTIVO';
    }
  };

  if (micBtn) {
    micBtn.addEventListener('click', window.__toggleListening);
  }

  function enableVoice() {
      // Manual — el usuario activa con el botón 🎤
      if (micBtn) {
        micBtn.title = 'CLIC PARA ACTIVAR VOZ';
      }
    }

    // ── Fin de initVoiceInput ──

  // Sin auto-activacion: el usuario activa manualmente con el boton 🎤

  window.addEventListener('agent-state', function(e) {
    if (e.detail === 'idle') {
      setTimeout(function() {
        if (isListening) startListening();
      }, 800);
    }
  });
}

  // ── 初始化打字動畫 ──
let lastUserActionTime = Date.now();
export function updateUserActivity() {
  lastUserActionTime = Date.now();
}

// ── 初始化 ──
export function initChat() {
  // 監聽外部模組的 terminal 訊息（解耦用，避免循環依賴）
  window.addEventListener('terminal-message', (e) => {
    const { message, isCommand } = e.detail;
    addTerminalMessage(message, isCommand);
  });

  if (chatSend) chatSend.addEventListener('click', handleChatSend);
  if (chatInput) {
    // IME 輸入中（注音/日文等）按 Enter 是確認選字，不送出
    chatInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.isComposing) handleChatSend();
    });

    // Ctrl+V / Cmd+V 貼圖支援
    chatInput.addEventListener('paste', (e) => {
      const items = Array.from(e.clipboardData?.items || []);
      const imageItems = items.filter(item => item.type.startsWith('image/'));
      if (!imageItems.length) return;

      e.preventDefault();
      const files = imageItems.map(item => item.getAsFile()).filter(Boolean);
      pendingFiles = [...pendingFiles, ...files];
      updateAttachBtn(pendingFiles.length);
      // 顯示通知
      addChatLine(`📋 ${files.length} imagen(es) pegada(s). Escribe un mensaje y envía.`, 'system-line');
    });
  }

  // 初始化系統訊息（config 已載入）
  const cfg = getConfig();
  const agentName = cfg?.agent?.name || 'JARVIS';
  const agentEmoji = cfg?.agent?.emoji || '🤖';

  // 直接顯示系統訊息，不用打字動畫
  setTimeout(() => {
    addChatLine(`SISTEMA INICIALIZADO. INTERFAZ ${agentName.toUpperCase()} EN LÍNEA.`, 'system-line');
  }, 1000);

  // 手機版：點 header 收合/展開聊天面板
  if (window.matchMedia('(max-width: 768px)').matches) {
    const chatHeader = document.querySelector('.terminal-panel.chat-panel .terminal-header');
    if (chatHeader) {
      let swiped = false;

      chatHeader.addEventListener('click', () => {
        if (swiped) { swiped = false; return; }
        const panel = document.querySelector('.terminal-panel.chat-panel');
        if (panel) {
          panel.classList.remove('chat-fullscreen');
          panel.classList.toggle('chat-collapsed');
        }
      });

      // 手機版：上滑 header 展開全螢幕，下滑縮回
      let touchStartY = 0;
      chatHeader.addEventListener('touchstart', (e) => {
        touchStartY = e.touches[0].clientY;
        swiped = false;
      }, { passive: true });
      chatHeader.addEventListener('touchend', (e) => {
        const deltaY = touchStartY - e.changedTouches[0].clientY;
        const panel = document.querySelector('.terminal-panel.chat-panel');
        if (!panel) return;
        if (deltaY > 50) {
          swiped = true;
          panel.classList.remove('chat-collapsed');
          panel.classList.add('chat-fullscreen');
        } else if (deltaY < -50) {
          swiped = true;
          panel.classList.remove('chat-fullscreen');
        }
      }, { passive: true });
    }
  }

  // 歷史訊息數量選擇器
  const historyLimit = document.getElementById('history-limit');
  if (historyLimit) {
    const saved = localStorage.getItem('jarvis-history-limit');
    if (saved) historyLimit.value = saved;
    historyLimit.addEventListener('change', () => {
      localStorage.setItem('jarvis-history-limit', historyLimit.value);
    });
  }

  // 載入歷史訊息，完成後再連 SSE
  loadHistory().then(() => {
    setTimeout(connectSSE, 500);
  });

  // 初始化 Model Status
  setTimeout(fetchModelStatus, 3500);

  // 檢查後端狀態
  setTimeout(async () => {
      try {
        const res = await fetch('/api/status');
        const data = await res.json();
        if (data.gateway) {
          addChatLine('GATEWAY OPENCLAW EN LÍNEA ✓', 'system-line');
        }
      } catch {
        addChatLine('BACKEND NO DISPONIBLE — MODO DEMO', 'system-line');
      }
    }, 3000);

    // Iniciar reconocimiento de voz (botón manual, sin auto-activar)
        setTimeout(initVoiceInput, 1500);

      // Botón minimizar/expandir chat
      const collapseBtn = document.getElementById('chat-collapse-btn');
      const chatPanel = document.querySelector('.terminal-panel.chat-panel');
      if (collapseBtn && chatPanel) {
        collapseBtn.addEventListener('click', function() {
          const isCollapsed = chatPanel.classList.toggle('chat-minimized');
          collapseBtn.textContent = isCollapsed ? '▸' : '▾';
          collapseBtn.title = isCollapsed ? 'EXPANDIR' : 'MINIMIZAR';
      
          // Si está minimizado, ocultar el content e input bar
          const content = chatPanel.querySelector('.terminal-content');
          const inputBar = chatPanel.querySelector('.chat-input-bar');
          if (content) content.style.display = isCollapsed ? 'none' : '';
          if (inputBar) inputBar.style.display = isCollapsed ? 'none' : '';
      
          // Guardar preferencia
          localStorage.setItem('houdini-chat-minimized', isCollapsed ? '1' : '0');
        });

        // Restaurar estado guardado
        if (localStorage.getItem('houdini-chat-minimized') === '1') {
          collapseBtn.click();
        }
      }
    }
