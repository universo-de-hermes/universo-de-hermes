/* Prueba el filtro por fechas y el panel de Pepe en Indicadores. */
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch({executablePath:'/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'});
  const p = await b.newPage({viewport:{width:1440,height:1100}});
  const errores = [];
  p.on('pageerror', e => errores.push('PAGEERROR: ' + e.message));
  await p.goto('https://agenda.universojota.tech/agenda.html');
  await p.waitForTimeout(2500);
  const campos = await p.$$('body input');
  if (campos.length >= 2){ await campos[0].fill('jhotas96@gmail.com');
                           await campos[1].fill('TzEi4LntP6I8TC'); }
  for (const bt of await p.$$('button'))
    if ((await bt.innerText()).trim().toLowerCase() === 'entrar'){ await bt.click(); break; }
  await p.waitForTimeout(4000);
  for (const el of await p.$$('a, button, div, span'))
    if ((await el.innerText() || '').trim() === 'Indicadores'){ try { await el.click(); break; } catch(e){} }
  await p.waitForTimeout(4000);

  const leer = () => p.evaluate(() => {
    const t = document.body.innerText || '';
    const i = t.indexOf('Quién agenda');
    const j = t.indexOf('Pepe · agente IA');
    return {
      subtitulo: (document.querySelector('.head .sub, .sub') || {}).innerText || '',
      desde: (document.querySelector('input[type=date]') || {}).value || '(no hay input date)',
      fechas: document.querySelectorAll('input[type=date]').length,
      botones: Array.prototype.map.call(document.querySelectorAll('button'),
        x => x.innerText.trim()).filter(s => /mes pasado|este mes|todo|limpiar/i.test(s)),
      reporte: i >= 0 ? t.slice(i, i + 300).replace(/\n+/g, ' | ') : '(sin reporte)',
      pepePanel: j >= 0 ? t.slice(j, j + 160).replace(/\n+/g, ' | ') : '(SIN panel de Pepe)'
    };
  });

  console.log('=== al entrar (mes en curso) ===');
  let v = await leer();
  console.log('   subtítulo:', v.subtitulo);
  console.log('   inputs de fecha:', v.fechas, '| desde:', v.desde);
  console.log('   botones del filtro:', v.botones);
  console.log('   reporte:', v.reporte);
  console.log('   panel Pepe:', v.pepePanel);

  for (const bt of await p.$$('button'))
    if ((await bt.innerText()).trim().toLowerCase() === 'mes pasado'){ await bt.click(); break; }
  await p.waitForTimeout(5000);
  console.log('\n=== despues de tocar «Mes pasado» ===');
  v = await leer();
  console.log('   subtítulo:', v.subtitulo);
  console.log('   inputs: desde =', v.desde);
  console.log('   reporte:', v.reporte);
  console.log('   panel Pepe:', v.pepePanel);
  await p.screenshot({path:'/tmp/agenda-rango.png'});

  for (const bt of await p.$$('button'))
    if ((await bt.innerText()).trim().toLowerCase() === 'todo'){ await bt.click(); break; }
  await p.waitForTimeout(6000);
  console.log('\n=== despues de tocar «Todo» ===');
  v = await leer();
  console.log('   subtítulo:', v.subtitulo);
  console.log('   reporte:', v.reporte);
  console.log('   panel Pepe:', v.pepePanel);
  await p.screenshot({path:'/tmp/agenda-todo.png'});

  console.log('\nERRORES DE JS:', errores.length ? errores : 'ninguno');
  await b.close();
})();
