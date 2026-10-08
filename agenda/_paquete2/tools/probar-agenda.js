/* La agenda del mostrador: lo que se cambió en el encargo 2.
     · el botón Recargar en todas las vistas
     · el mes y los reportes en el reloj de 12 s, solo cuando se están mirando
     · que no se apilen peticiones
     · los cupos apartados dibujados en el día
     · y que si el servidor TODAVÍA no sirve /reservas, nada se rompa

   Se corre:  node probar-agenda.js      (necesita la agenda viva en :8001) */
const {chromium} = require('playwright');
const http = require('http'), fs = require('fs');
const PAGINA = '/var/www/html/agenda.html', PUERTO = 8975, API = 8001;
let ok = 0, mal = 0;
const t = (n, c, e) => { if (c) { ok++; console.log('  ok   ' + n); }
  else { mal++; console.log('  MAL  ' + n + (e ? '\n       ' + String(e).slice(0,400) : '')); } };

/* el servidor de verdad todavía no tiene /reservas: aquí se simula, para
   poder probar las dos caras — cuando responde y cuando no existe */
let sirveReservas = false, pedidos = {reservas:0, agenda:0, citas:0};
const APARTADO = () => {
  /* Se devuelve expira_en SIN zona —como lo guarda Postgres— y además
     quedan_minutos ya calculado. Así la prueba comprueba que la agenda usa la
     cuenta del servidor y no se pone a restar fechas, que es donde se cuelan
     las cinco horas de diferencia. */
  const en = new Date(Date.now() + 7*60000).toISOString().slice(0,19).replace('T',' ');
  return JSON.stringify({reservas:[{id:'r1', especialista_id:'__ESP__',
    sede_id:'__SEDE__', fecha:'__HOY__', inicio:'11:00:00', fin:'11:30:00',
    canal:'Autoservicio', expira_en: en, quedan_minutos: 7}]});
};
let ESP = '', SEDE = '', HOY = new Date().toISOString().slice(0,10);

const srv = http.createServer((q, r) => {
  if (q.url.startsWith('/api/')){
    const ruta = q.url.slice(4);
    if (ruta.indexOf('/reservas') >= 0){
      pedidos.reservas++;
      if (!sirveReservas){ r.writeHead(404, {'content-type':'application/json'});
                           return r.end('{"detail":"no existe"}'); }
      r.writeHead(200, {'content-type':'application/json'});
      return r.end(APARTADO().replace('__ESP__',ESP).replace('__SEDE__',SEDE).replace('__HOY__',HOY));
    }
    if (ruta.indexOf('/agenda/') >= 0) pedidos.agenda++;
    if (ruta.indexOf('/citas?') >= 0) pedidos.citas++;
    const x = http.request({host:'127.0.0.1', port:API, path:ruta,
      method:q.method, headers:q.headers}, y => { r.writeHead(y.statusCode, y.headers); y.pipe(r); });
    x.on('error', () => { r.writeHead(502); r.end('{}'); }); q.pipe(x); return;
  }
  fs.readFile(PAGINA, (e,b) => { r.writeHead(200,{'content-type':'text/html; charset=utf-8'}); r.end(b); });
});

(async () => {
  await new Promise(r => srv.listen(PUERTO, r));
  const nav = await chromium.launch({executablePath:'/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'});
  const ctx = await nav.newContext({viewport:{width:1440, height:900}});
  const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(String(e)));
  p.on('console', m => { if (m.type()==='error' && !/favicon|404|401/.test(m.text())) errs.push(m.text()); });

  await p.goto(`http://localhost:${PUERTO}/agenda.html?api=http://localhost:${PUERTO}`);
  await p.waitForTimeout(2500);
  const hayEntrada = await p.evaluate(() =>
    !!document.querySelector('input[type="password"]'));
  if (hayEntrada){
    await p.locator('input[type="email"],input[type="text"]').first().fill('jhotas96@gmail.com');
    await p.locator('input[type="password"]').first().fill('TzEi4LntP6I8TC');
    await p.locator('button', {hasText:/Entrar|Ingresar|Continuar/}).first().click();
    await p.waitForTimeout(3500);
  }
  t('la agenda abre', await p.evaluate(() => !!document.querySelector('#grid, #view .g')),
    (await p.evaluate(() => document.body.innerText)).slice(0,200));

  ESP = await p.evaluate(() => { const c = document.querySelector('.gcol[data-esp]');
    return c ? c.getAttribute('data-esp') : ''; });
  SEDE = await p.evaluate(() => (typeof S !== 'undefined' && S.sede) || '');
  HOY = await p.evaluate(() => (typeof S !== 'undefined' && S.fecha) || '');

  console.log('\n— el botón Recargar —');
  t('está en la vista del día',
    await p.evaluate(() => !!document.querySelector('#b-recargar')));
  for (const v of ['clientes','indicadores','especialistas','sedes','servicios','ajustes']){
    await p.evaluate(k => irA(k), v);
    await p.waitForTimeout(700);
    t(`también en «${v}»`, await p.evaluate(() => !!document.querySelector('#b-recargar')));
  }

  console.log('\n— el mes se pide fresco al abrirlo —');
  await p.evaluate(() => irA('agenda'));  await p.waitForTimeout(600);
  const antes = await p.evaluate(() => pedidos_citas_contador || 0).catch(()=>0);
  const c0 = pedidos.citas;
  await p.evaluate(() => irA('indicadores'));
  await p.waitForTimeout(2500);
  t('al entrar a indicadores pide el mes al servidor', pedidos.citas > c0,
    `antes ${c0}, ahora ${pedidos.citas}`);
  const c1 = pedidos.citas;
  await p.evaluate(() => irA('indicadores'));
  await p.waitForTimeout(2500);
  t('y al volver a entrar lo vuelve a pedir, no se queda con lo viejo',
    pedidos.citas > c1, `antes ${c1}, ahora ${pedidos.citas}`);

  console.log('\n— el reloj mira solo la vista que está en pantalla —');
  await p.evaluate(() => { REFRESCO_PRUEBA = true; });
  const a2 = pedidos.agenda, b2 = pedidos.citas;
  await p.waitForTimeout(14000);                 /* un tic del reloj, en indicadores */
  t('en indicadores refresca el MES, no el día',
    pedidos.citas > b2 && pedidos.agenda === a2,
    `día ${a2}→${pedidos.agenda} · mes ${b2}→${pedidos.citas}`);
  await p.evaluate(() => irA('agenda'));
  await p.waitForTimeout(1500);
  const a3 = pedidos.agenda, b3 = pedidos.citas;
  await p.waitForTimeout(14000);                 /* otro tic, ahora en el día */
  t('en el día refresca el DÍA, no el mes',
    pedidos.agenda > a3 && pedidos.citas === b3,
    `día ${a3}→${pedidos.agenda} · mes ${b3}→${pedidos.citas}`);

  console.log('\n— no se apilan peticiones —');
  const a4 = pedidos.agenda;
  await p.evaluate(() => { for (let i=0;i<6;i++) refrescarVista({aMano:true}); });
  await p.waitForTimeout(2500);
  t('seis toques seguidos a Recargar = una sola carga',
    pedidos.agenda - a4 <= 1, `${a4} → ${pedidos.agenda}`);

  console.log('\n— los cupos apartados —');
  t('sin el endpoint, la agenda sigue funcionando igual',
    await p.evaluate(() => !!document.querySelector('#grid')) && errs.length === 0,
    errs.join('\n'));
  t('y no insiste: lo pide una vez y se calla', pedidos.reservas <= 3, pedidos.reservas);

  sirveReservas = true;
  await p.evaluate(() => { window.__api.reintentarApartados(); });
  await p.evaluate(() => refrescarVista({aMano:true}));
  await p.waitForTimeout(2500);
  const ap = await p.evaluate(() => {
    const e = document.querySelector('.cita.apartado');
    return e ? {texto:e.innerText.replace(/\n/g,' · '), titulo:e.getAttribute('title')} : null;
  });
  t('cuando el servidor los sirve, se dibujan en el día', !!ap, ap);
  t('y dicen cuánto les queda, con la cuenta del servidor',
    ap && /vence en 7 minutos/.test(ap.texto), ap && ap.texto);
  t('con una explicación al pasar el cursor',
    ap && /tablet/i.test(ap.titulo || ''), ap && ap.titulo);
  await p.screenshot({path:'/tmp/agenda-apartado.png'});

  t('sin errores de JavaScript', errs.length === 0, errs.join('\n'));
  await nav.close(); srv.close();
  console.log(`\n${ok} ok, ${mal} mal`);
  process.exit(mal ? 1 : 0);
})();
