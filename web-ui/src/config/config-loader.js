// ── Frontend config loader ──
// Loads from /api/config (backend), falls back to /config.json directly

let _config = null;

export async function loadConfig() {
  if (_config) return _config;

  // 1. Try backend API
  try {
    const res = await fetch('/api/config');
    if (res.ok) {
      _config = await res.json();
      return _config;
    }
  } catch {}

  // 2. Fallback: fetch config.json directly (Vite serves it from project root)
  try {
    const res = await fetch('/config.json');
    if (res.ok) {
      _config = await res.json();
      return _config;
    }
  } catch {}

  // 3. Last resort: hardcoded default
  _config = { name: 'HOUDINI', agent: { name: 'HOUDINI', emoji: '🤖', skills: [] }, theme: {} };
  return _config;
}

export function getConfig() {
  return _config;
}