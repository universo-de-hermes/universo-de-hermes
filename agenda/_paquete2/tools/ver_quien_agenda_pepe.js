/* Entra a la agenda, abre Indicadores, cambia el mes a SEPTIEMBRE y lee el
   reporte "Quién agenda" — para ver si Pepe aparece ahí. */
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch({executablePath:'/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'});
  const p = await b.newPage({viewport:{width:1440,height:1000}});
  const errores = [];
  p.on('pageerror', e => errores.push('PAGEERROR: ' + e.message));
  await p.goto('https://agenda.universojota.tech/agenda.html');
  await p.waitForTimeout(2500);

  const campos = await p.$$('body input');
  if (campos.length >= 2){
    await campos[0].fill('jhotas96@gmail.com');
    await campos[1].fill('TzEi4LntP6I8TC');
  }
  for (const bt of await p.$$('button')){
    if ((await bt.innerText()).trim().toLowerCase() === 'entrar'){ await bt.click(); break; }
  }
  await p.waitForTimeout(4000);

  /* abrir Indicadores */
  for (const el of await p.$$('a, button, div, span')){
    const s = (await el.innerText() || '').trim();
    if (s === 'Indicadores'){ try { await el.click(); break; } catch(e){} }
  }
  await p.waitForTimeout(3500);

  const leer = () => p.evaluate(() => {
    const t = document.body.innerText || '';
    const i = t.indexOf('Quién agenda');
    return {mes: (document.querySelector('input[type=month]')||{}).value || '(no hay input month)',
            bloque: i >= 0 ? t.slice(i, i + 460) : '(no encontre el reporte)'};
  });

  console.log('=== 1. como esta (mes en curso) ===');
  let v = await leer();
  console.log('   mes:', v.mes);
  console.log(v.bloque.split('\n').map(s=>'   '+s).join('\n'));

  const cambio = await p.evaluate(() => {
    const m = document.querySelector('input[type=month]');
    if (m){ m.value = '2026-09';
            m.dispatchEvent(new Event('input',{bubbles:true}));
            m.dispatchEvent(new Event('change',{bubbles:true}));
            return 'cambie el mes a 2026-09'; }
    const s = document.querySelector('select');
    if (s){ for (const o of s.options) if (/2026-09|septiembre/i.test(o.text) || /2026-09/.test(o.value)){
              s.value = o.value; s.dispatchEvent(new Event('change',{bubbles:true})); return 'cambie el select a ' + o.text; } }
    return 'NO encontre el control del mes';
  });
  console.log('\n=== 2. ' + cambio + ' ===');
  await p.waitForTimeout(4000);
  v = await leer();
  console.log('   mes:', v.mes);
  console.log(v.bloque.split('\n').map(s=>'   '+s).join('\n'));
  console.log('\nERRORES DE JS:', errores.length ? errores : 'ninguno');
  await p.screenshot({path:'/tmp/agenda-septiembre.png'});
  await b.close();
})();
