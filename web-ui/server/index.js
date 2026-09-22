// ── HOUDINI Backend — standalone (no OpenClaw Gateway) ──

import express from 'express';
import path from 'path';
import os from 'os';
import { readFile, writeFile } from 'fs/promises';
import { fileURLToPath } from 'url';

import { addClient, removeClient, broadcastSystem } from './sse.js';
import { initTTS } from './tts.js';

// Routes
import chatRoutes from './routes/chat.js';
import statusRoutes from './routes/status.js';
import ttsRoutes from './routes/tts-routes.js';
import tasksRoutes from './routes/tasks.js';
import skillsRoutes from './routes/skills.js';
import memoryRoutes from './routes/memory.js';
import scheduleRoutes from './routes/schedule.js';
import voiceRoutes from './routes/voice.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');

// ── Load config ──
let config;
try {
  config = JSON.parse(await readFile(path.join(ROOT, 'config.local.json'), 'utf-8'));
} catch {
  config = JSON.parse(await readFile(path.join(ROOT, 'config.json'), 'utf-8'));
}

const PORT = process.env.PORT || config.server.port || 9999;
const SESSION_KEY = config.agent.sessionKey;

// ── Express ──
const app = express();
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ extended: true, limit: '50mb' }));
app.locals.sessionKey = SESSION_KEY;

// ── CORS for Vite dev server ──
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.sendStatus(200);
  next();
});

// ── SSE endpoint ──
app.get('/api/events', (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache',
    Connection: 'keep-alive', 'Access-Control-Allow-Origin': '*',
  });
  res.write('data: {"type":"connected"}\n\n');
  addClient(res);
  req.on('close', () => removeClient(res));
});

// ── Config endpoint (for frontend loader) ──
app.get('/api/config', (req, res) => {
  res.json(config);
});

// ── Mount routes ──
app.use('/api', chatRoutes);
app.use('/api', statusRoutes(config, null));
app.use('/api', ttsRoutes);
app.use('/api', tasksRoutes);
app.use('/api', skillsRoutes);
app.use('/api', memoryRoutes);
app.use('/api', scheduleRoutes);
app.use('/api', voiceRoutes);

// ── Initialize ──
initTTS(config.tts);

// System stats emitter
let sysInterval = null;
function startSystemEmitter() {
  const startTime = Date.now();
  const cpus = os.cpus();
  
  const sendStats = () => {
    const mem = process.memoryUsage();
    const totalMem = os.totalmem();
    const freeMem = os.freemem();
    const uptime = Math.floor((Date.now() - startTime) / 1000);
    
    broadcastSystem({
      cpu: Math.round((1 - freeMem / totalMem) * 100),
      mem: {
        total: (totalMem / (1024 ** 3)).toFixed(1),
        used: ((totalMem - freeMem) / (1024 ** 3)).toFixed(1),
      },
      uptime,
      procs: cpus.length,
    });
  };
  
  sendStats();
  sysInterval = setInterval(sendStats, 5000);
}

startSystemEmitter();

// ── Listen ──
app.listen(PORT, () => {
  console.log(`[HOUDINI] API server en http://localhost:${PORT}`);
  console.log(`[HOUDINI] Sirviendo configuración desde /api/config`);
  console.log(`[HOUDINI] Frontend Vite en http://localhost:8001`);
});

export { config };