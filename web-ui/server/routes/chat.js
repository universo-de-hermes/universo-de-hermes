// ── Chat Routes: relay to Houdini Python Bridge ──

import { Router } from 'express';
import multer from 'multer';
import os from 'os';
import path from 'path';
import http from 'http';
import { broadcastChat } from '../sse.js';

const router = Router();
const fileUpload = multer({ dest: os.tmpdir(), limits: { fileSize: 20 * 1024 * 1024 } });

const BRIDGE_HOST = '127.0.0.1';
const BRIDGE_PORT = 9876;

let msgCountToday = 0;
let msgCountDate = new Date().toLocaleDateString('es');

export function getMsgCount() { return msgCountToday; }
export function getMsgCountDate() { return msgCountDate; }

function bumpMsgCount() {
  const today = new Date().toLocaleDateString('es');
  if (today !== msgCountDate) { msgCountToday = 0; msgCountDate = today; }
  msgCountToday++;
}

function callBridge(endpoint, data) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify(data);
    const options = {
      hostname: BRIDGE_HOST,
      port: BRIDGE_PORT,
      path: endpoint,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(body),
      },
      timeout: 120000,
    };

    const req = http.request(options, (res) => {
      let responseData = '';
      res.on('data', chunk => responseData += chunk);
      res.on('end', () => {
        try {
          resolve(JSON.parse(responseData));
        } catch {
          resolve({ error: 'invalid bridge response', raw: responseData });
        }
      });
    });

    req.on('error', (err) => reject(err));
    req.on('timeout', () => { req.destroy(); reject(new Error('bridge timeout')); });
    req.write(body);
    req.end();
  });
}

// Upload with files
router.post('/chat/upload', fileUpload.array('files', 10), async (req, res) => {
  const message = req.body.message || '';
  const files = req.files || [];
  if (!files.length && !message) return res.status(400).json({ error: 'no files or message' });

  try {
    const fileNames = files.map(f => f.originalname).join(', ');
    const fullMessage = message ? `${message} [📎 ${fileNames}]` : `📎 ${fileNames}`;
    bumpMsgCount();

    // Forward to bridge
    const bridgeRes = await callBridge('/chat', { message: fullMessage });
    const runId = `houdini-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;

    res.json({
      ok: true,
      runId,
      files: files.map(f => f.originalname),
      text: bridgeRes.text || '',
      error: bridgeRes.error || null,
    });
  } catch (err) {
    res.status(502).json({ error: err.message || 'bridge error' });
  }
});

// Send message
router.post('/chat', async (req, res) => {
  const { message, session_id } = req.body;
  if (!message) return res.status(400).json({ error: 'message required' });

  bumpMsgCount();
  try {
    const bridgeRes = await callBridge('/chat', { message, session_id: session_id || 'default' });
    const runId = `houdini-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;

    // Broadcast to web UI via SSE
    if (bridgeRes.text) {
      broadcastChat({
        runId,
        state: 'from_assistant',
        text: bridgeRes.text,
        text_user: message,
        role: 'assistant',
        done: true,
      });
    }

    res.json({
      ok: true,
      runId,
      text: bridgeRes.text || '',
      tool_calls: bridgeRes.tool_calls || [],
      error: bridgeRes.error || null,
    });
  } catch (err) {
    res.status(502).json({ error: err.message || 'bridge error' });
  }
});

// History
router.get('/history', async (req, res) => {
  res.json({ messages: [] });
});

// Abort
router.post('/abort', async (req, res) => {
  res.json({ ok: true });
});

// Model status
router.get('/model-status', (req, res) => {
  res.json({
    model: 'Claude Sonnet 4.5',
    provider: 'Anthropic (Houdini)',
    contextWindow: 128000,
    usage: { input: 0, output: 0 },
    totalTokens: 0,
  });
});

// Sync endpoint: el asistente de escritorio envía aquí para mostrar en la web
router.post('/sync', async (req, res) => {
  const { text_user, text_response } = req.body;
  if (text_response) {
    broadcastChat({
      runId: `sync-${Date.now()}`,
      state: 'from_assistant',
      text: text_response,
      text_user: text_user || '',
      role: 'assistant',
      done: true,
    });
  }
  res.json({ ok: true });
});

// Profile endpoints
router.post('/profile/save', async (req, res) => {
  try {
    const bridgeRes = await callBridge('/profile/save', req.body);
    res.json(bridgeRes);
  } catch (err) {
    res.status(502).json({ error: err.message });
  }
});

router.post('/profile/delete', async (req, res) => {
  try {
    const bridgeRes = await callBridge('/profile/delete', req.body);
    res.json(bridgeRes);
  } catch (err) {
    res.status(502).json({ error: err.message });
  }
});

router.get('/profile', async (req, res) => {
  try {
    // The bridge /profile expects POST, but we can GET via a simple relay
    const bridgeRes = await callBridge('/profile', {});
    res.json(bridgeRes);
  } catch (err) {
    res.status(502).json({ error: err.message });
  }
});

export default router;