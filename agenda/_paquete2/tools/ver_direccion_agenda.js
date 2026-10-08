/* Entra a la agenda y mira si la direccion aparece a la vista o solo el nombre. */
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch({executablePath:'/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'});
  const p = await b.newPage({viewport:{width:1440,height:900}});
  const errores = [];
  p.on('pageerror', e => errores.push('PAGEERROR: ' + e.message));
  await p.goto('https://agenda.universojota.tech/agenda.html');
  await p.waitForTimeout(2500);

  const campos = await p.$$('#vista input, body input');
  if (campos.length >= 2){
    await campos[0].fill('jhotas96@gmail.com');
    try { await p.fill('#e-clave', 'TzEi4LntP6I8TC'); } catch(e){ await campos[1].fill('TzEi4LntP6I8TC'); }
  }
  for (const bt of await p.$$('button')){
    if ((await bt.innerText()).trim().toLowerCase() === 'entrar'){ await bt.click(); break; }
  }
  await p.waitForTimeout(4000);

  const ver = async () => p.evaluate(() => {
    const t = document.body.innerText || '';
    return {
      hay_direccion: t.indexOf('Cra 11A') >= 0 || t.indexOf('Cra 25A') >= 0,
      lineas: t.split('\n').map(s => s.trim()).filter(Boolean).slice(0, 22)
    };
  });

  console.log('=== 1. la agenda abierta ===');
  let v = await ver();
  console.log('   ¿se ve alguna direccion en pantalla?:', v.hay_direccion ? 'SI' : 'NO');
  console.log('   lo que se ve:', JSON.stringify(v.lineas.slice(0, 14)));
  await p.screenshot({path:'/tmp/agenda-abierta.png'});

  console.log('\n=== 2. la pagina de Sedes ===');
  for (const el of await p.$$('a, button, div')){
    const s = (await el.innerText() || '').trim();
    if (s === 'Sedes'){ try { await el.click(); break; } catch(e){} }
  }
  await p.waitForTimeout(2500);
  v = await ver();
  console.log('   ¿se ve alguna direccion en pantalla?:', v.hay_direccion ? 'SI' : 'NO');
  console.log('   lo que se ve:', JSON.stringify(v.lineas.slice(0, 16)));
  await p.screenshot({path:'/tmp/agenda-sedes.png'});

  console.log('\nERRORES DE JS:', errores.length ? errores : 'ninguno');
  await b.close();
})();
