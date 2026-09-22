// ── Status Routes: /api/config, /api/status, /api/model-status ──

import { Router } from 'express';
import { getMsgCount } from './chat.js';

const router = Router();

export default function statusRoutes(config, _ocConfigPath) {
  // Frontend config
  router.get('/config', (req, res) => {
    res.json({ name: config.name, agent: config.agent, theme: config.theme });
  });

  // Health check
  router.get('/status', async (req, res) => {
    res.json({
      gateway: false,
      sessionKey: config.agent?.sessionKey || null,
      channel: 'Hermes Desktop',
      msgCount: getMsgCount(),
    });
  });

  // Model Status — static info (no Gateway needed)
  router.get('/model-status', async (req, res) => {
    res.json({
      model: 'HOUDINI',
      provider: 'Hermes Agent',
      contextWindow: 128000,
      totalTokens: 0,
      usage: { input: 0, output: 0 },
    });
  });

  return router;
}