// ── Schedule Routes: standalone (no OpenClaw) ──

import { Router } from 'express';
import { broadcastEvent } from '../sse.js';

const router = Router();

router.get('/schedule', async (req, res) => {
  res.json({
    heartbeat: { every: '30m', enabled: true, content: '' },
    jobs: [{
      id: 'houdini-bridge',
      name: 'Bridge Houdini',
      enabled: true,
      schedule: { expr: '0 */12 * * *', kind: 'cron' },
      lastRun: null,
      lastStatus: null,
      nextRun: null,
    }],
  });
});

router.patch('/schedule/:id', async (req, res) => {
  const { enabled } = req.body;
  if (typeof enabled !== 'boolean') return res.status(400).json({ error: 'enabled (boolean) required' });
  broadcastEvent('schedule-update');
  res.json({ ok: true });
});

export default router;