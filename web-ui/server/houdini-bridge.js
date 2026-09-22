// ── HOUDINI BRIDGE SERVER ──
// Sirve el frontend JARVIS y conecta el chat con Houdini

import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import WebSocket from 'ws';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = __dirname;
const DIST = path.join(ROOT, '..', 'dist');
const PORT = process.env.PORT || 8001;

// ── HOUDINI WebSocket ──
const HOUDINI_WS = process.env.HOUDINI_WS || 'ws://127.0.0.1:3000/ws';
let hws = null;
let hwsReady = false;
let chatQueue = [];

function connectHoudini() {
  if (hws) try { hws.close(); } catch {}
  
  console.log(`[HOUDINI] Conectando a ${HOUDINI_WS}...`);
  hws = new WebSocket(HOUDINI_WS);
  hwsReady = false;

  hws.on('open', () => {
    console.log('[HOUDINI] ✅ Conectado!');
    hwsReady = true;
    // Enviar mensajes encolados
    for (const q of chatQueue) {
      hws.send(JSON.stringify({ type: 'chat', payload: { text: q.text }, timestamp: Date.now() }));
    }
    chatQueue = [];
  });

  hws.on('message', (raw) => {
    try {
      const msg = JSON.parse(raw.toString());
      console.log('[HOUDINI] Mensaje:', msg.type);
      
      if (msg.type === 'chat_response' && msg.payload?.text) {
        // Enviar a todos los clientes SSE
        broadcastToClients({
          type: 'chat',
          text: msg.payload.text,
          done: true,
          runId: Date.now().toString(),
        });
      }
      
      if (msg.type === 'handshake_ack') {
        console.log('[HOUDINI] Handshake OK');
      }
    } catch (e) {
      console.error('[HOUDINI] Error parseando mensaje:', e.message);
    }
  });

  hws.on('close', () => {
    console.log('[HOUDINI] Desconectado. Reintentando en 3s...');
    hwsReady = false;
    setTimeout(connectHoudini, 3000);
  });

  hws.on('error', (err) => {
    console.error('[HOUDINI] Error WS:', err.message);
  });
}

function sendToHoudini(text) {
  const msg = JSON.stringify({ type: 'chat', payload: { text }, timestamp: Date.now() });
  if (hwsReady && hws) {
    hws.send(msg);
  } else {
    chatQueue.push({ text });
  }
}

// ── SSE (Server-Sent Events) ──
let sseClients = [];

function broadcastToClients(data) {
  const msg = `data: ${JSON.stringify(data)}\n\n`;
  for (const client of sseClients) {
    try { client.write(msg); } catch {}
  }
}

// ── Express ──
const app = express();
app.use(express.json());

// API: Status
app.get('/api/status', (req, res) => {
  res.json({
    gateway: hwsReady,
    uptime: process.uptime(),
    version: 'houdini-bridge-1.0',
  });
});

// API: Model Status
app.get('/api/model-status', (req, res) => {
  res.json({
    model: 'HOUDINI',
    provider: 'deepseek',
    contextWindow: 128000,
    usage: { input: 0, output: 0 },
    totalTokens: 0,
  });
});

// API: Chat
app.post('/api/chat', (req, res) => {
  const { message } = req.body || {};
  if (!message) return res.status(400).json({ error: 'message required' });
  
  const runId = Date.now().toString();
  
  // Enviar a Houdini
  sendToHoudini(message);
  
  res.json({ runId, ok: true });
});

// API: Chat Upload (simplificado)
app.post('/api/chat/upload', (req, res) => {
  res.json({ runId: Date.now().toString(), ok: true });
});

// API: History
app.get('/api/history', (req, res) => {
  res.json({ messages: [] });
});

// API: SSE Events
app.get('/api/events', (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    Connection: 'keep-alive',
    'Access-Control-Allow-Origin': '*',
  });
  res.write(`data: ${JSON.stringify({ type: 'connected' })}\n\n`);
  sseClients.push(res);
  req.on('close', () => {
    sseClients = sseClients.filter(c => c !== res);
  });
});

// API: TTS (simplificado - la voz la maneja el frontend)
app.post('/api/tts', async (req, res) => {
  const { text } = req.body || {};
  if (!text) return res.status(400).json({ error: 'text required' });
  // Devolvemos success, el frontend reproduce con Web Speech API
  res.json({ ok: true, engine: 'system' });
});

// API: TTS Engines
app.get('/api/tts/engines', (req, res) => {
  res.json({ engines: ['system'], current: 'system' });
});

// API: Tasks, Skills, Memory, Schedule (stubs)
app.get('/api/tasks', (req, res) => res.json({ tasks: [] }));
app.post('/api/tasks', (req, res) => res.json({ ok: true }));
app.get('/api/skills', (req, res) => res.json({ skills: [] }));
app.get('/api/memory', (req, res) => res.json({ memories: [] }));
app.get('/api/schedule', (req, res) => res.json({ events: [] }));
app.post('/api/tts', (req, res) => res.json({ ok: true }));
app.get('/api/voice/status', (req, res) => res.json({ status: 'idle', vad: false }));
app.post('/api/voice/command', (req, res) => res.json({ ok: true }));

// ── Static Files ──
app.use(express.static(DIST));
// Catch-all para SPA: cualquier ruta que no sea /api sirve index.html
app.use((req, res, next) => {
  if (req.path.startsWith('/api')) return next();
  res.sendFile(path.join(DIST, 'index.html'));
});

// ── Inicio ──
connectHoudini();

app.listen(PORT, () => {
  console.log(`[HOUDINI BRIDGE] Sirviendo JARVIS en http://localhost:${PORT}`);
  console.log(`[HOUDINI BRIDGE] Conectado a Houdini WS: ${HOUDINI_WS}`);
});