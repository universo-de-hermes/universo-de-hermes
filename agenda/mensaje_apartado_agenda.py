#!/usr/bin/env python3
"""El error que ve RECEPCION cuando la tablet/el bot tienen la hora apartada."""
import io, re, shutil, subprocess

AG = "/var/www/html/agenda.html"

VIEJO = '  CUPO_APARTADO:    "Otra persona está tomando ese horario en este momento.",'
NUEVO = ('  /* Cuando la tablet (o el bot) tienen la hora apartada mientras la clienta\n'
         '     decide. Recepción tiene que poder entender que NO es un choque raro:\n'
         '     alguien la está reservando ahora mismo y se libera sola. */\n'
         '  CUPO_APARTADO:    "Esa cita la está reservando otro usuario en este momento "\n'
         '                    + "(tablet o WhatsApp). Espera un minuto, o escoge otra hora.",')

raw = open(AG, "rb").read()
vb = VIEJO.encode("utf-8")
n = raw.count(vb)
print("coincidencias:", n)
if n != 1:
    print("ABORTO: no es exactamente 1"); raise SystemExit(1)
shutil.copy2(AG, AG + ".pre-msg-apartado.bak")
open(AG, "wb").write(raw.replace(vb, NUEVO.encode("utf-8")))
print("cambiado. respaldo:", AG + ".pre-msg-apartado.bak")

print("\n=== verificacion ===")
h = io.open(AG, encoding="utf-8", errors="replace").read()
bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", h, re.S | re.I)
io.open("/tmp/chk_ag.js", "w", encoding="utf-8").write("\n;\n".join(bloques))
r = subprocess.run(["node", "--check", "/tmp/chk_ag.js"], capture_output=True, text=True)
print("   JS de la agenda:", "OK" if r.returncode == 0 else "MAL " + r.stderr[-400:])
print("   el texto viejo debe dar 0:", h.count("Otra persona está tomando ese horario"))

# ── el mensaje REAL que sale en pantalla ──────────────────────────────────
js = r'''
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch({executablePath:'/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'});
  const p = await b.newPage();
  await p.goto('file:///var/www/html/agenda.html');
  await p.waitForTimeout(600);
  const r = await p.evaluate(() => ({
    apartado: mensajeDeError({detail:"CUPO_APARTADO: otra conversación está tomando ese horario"}, "", 409),
    tomado:   mensajeDeError({detail:"CUPO_TOMADO: ya hay una cita en ese horario"}, "", 409)
  }));
  console.log("   CUPO_APARTADO (la hora apartada) -> " + JSON.stringify(r.apartado));
  console.log("   CUPO_TOMADO   (ya hay cita)      -> " + JSON.stringify(r.tomado));
  await b.close();
})();
'''
io.open("/root/universo/agenda/_paquete2/tools/msg_agenda.js", "w").write(js)
r = subprocess.run(["node", "msg_agenda.js"], capture_output=True, text=True,
                   cwd="/root/universo/agenda/_paquete2/tools")
print(r.stdout or r.stderr[-500:])
