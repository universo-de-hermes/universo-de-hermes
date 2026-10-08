
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
