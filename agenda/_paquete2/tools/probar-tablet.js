/* Lo que pide el encargo y no medía nadie:
     · todo botón de 44px de alto para arriba
     · ningún texto con poco contraste sobre el vidrio oscuro
     · que la página siga entera en un Safari 12 (iPad iOS 12.5.8)

   El Safari 12 se simula quitando del CSS lo que ese navegador no entiende
   —color-mix(), clamp(), gap en flex, 100dvh, aspect-ratio— que es
   exactamente lo que le pasa al archivo cuando llega al aparato. */
const {chromium} = require('playwright');
const http = require('http'), fs = require('fs');
const PAGINA = '/var/www/html/autoservicio.html', PUERTO = 8971, API = 8001;
let ok = 0, mal = 0;
const t = (n, c, e) => { if (c) { ok++; console.log('  ok   ' + n); }
  else { mal++; console.log('  MAL  ' + n + (e ? '\n       ' + String(e).slice(0,400) : '')); } };

/* contraste de la WCAG: 4.5 para texto normal, 3 para texto grande */
function luz(c){
  const m = String(c).match(/[\d.]+/g); if (!m) return null;
  const [r,g,b] = m.slice(0,3).map(Number);
  const f = v => { v /= 255; return v <= .03928 ? v/12.92 : Math.pow((v+.055)/1.055, 2.4); };
  return .2126*f(r) + .7152*f(g) + .0722*f(b);
}
const razon = (a,b) => { const [x,y] = [luz(a), luz(b)].sort((p,q)=>q-p);
  return (x + .05) / (y + .05); };

function viejo(html){
  return html
    .replace(/[a-z-]+\s*:[^;{}]*color-mix\([^;{}]*\)[^;{}]*;/g, '')
    .replace(/[a-z-]+\s*:[^;{}]*clamp\([^;{}]*\)[^;{}]*;/g, '')
    .replace(/[a-z-]+\s*:[^;{}]*\bdvh\b[^;{}]*;?/g, '')
    .replace(/aspect-ratio\s*:[^;{}]*;?/g, '')
    /* gap sí existe en grid en Safari 12; en FLEX es lo que se ignora.
       Aquí se quita siempre: es el peor caso y así se ve si aguanta. */
    .replace(/(^|[;{])\s*gap\s*:[^;{}]*;?/g, '$1');
}

const crudo = fs.readFileSync(PAGINA, 'utf8');
const srv = http.createServer((q,r) => {
  if (q.url.startsWith('/api/')){
    const x = http.request({host:'127.0.0.1', port:API, path:q.url.slice(4),
      method:q.method, headers:q.headers}, y => { r.writeHead(y.statusCode, y.headers); y.pipe(r); });
    x.on('error', () => { r.writeHead(502); r.end('{}'); }); q.pipe(x); return;
  }
  const html = q.url.indexOf('viejo') >= 0 ? viejo(crudo) : crudo;
  r.writeHead(200, {'content-type':'text/html; charset=utf-8'}); r.end(html);
});

const MEDIR = () => {
  const bajos = [], chicos = [];
  const fondoDe = (el) => {
    let n = el;
    while (n && n !== document.documentElement){
      const cs = getComputedStyle(n);
      /* El botón principal se pinta con un degradado: ahí backgroundColor va
         en transparente y, sin esto, se comparaba su letra contra el fondo de
         la tarjeta de atrás. Se toma el primer color del degradado. */
      if (cs.backgroundImage && cs.backgroundImage !== 'none'){
        const c = cs.backgroundImage.match(/rgba?\([^)]+\)/);
        if (c) return c[0];
      }
      const b = cs.backgroundColor;
      const a = (b.match(/[\d.]+/g) || [])[3];
      if (b && b !== 'transparent' && a !== '0') return b;
      n = n.parentElement;
    }
    return getComputedStyle(document.body).backgroundColor;
  };
  document.querySelectorAll('button, .btn, input, select').forEach(el => {
    if (el.closest('[hidden]')) return;
    const c = el.getBoundingClientRect();
    if (!c.width && !c.height) return;
    if (c.height < 44) chicos.push(Math.round(c.height) + 'px · ' + (el.innerText||el.id||el.tagName).slice(0,24));
  });
  document.querySelectorAll('h1,h2,p,span,div,label,button,.sub,.pie,.d,.t').forEach(el => {
    if (el.closest('[hidden]')) return;
    const txt = (el.childNodes.length && [...el.childNodes]
      .filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join('')) || '';
    if (txt.length < 3) return;
    const cs = getComputedStyle(el);
    const px = parseFloat(cs.fontSize), grueso = parseInt(cs.fontWeight) >= 600;
    const grande = px >= 24 || (px >= 18.66 && grueso);
    bajos.push({txt: txt.slice(0,34), color: cs.color, fondo: fondoDe(el),
                px: Math.round(px), minimo: grande ? 3 : 4.5});
  });
  return {chicos, bajos};
};

(async () => {
  await new Promise(r => srv.listen(PUERTO, r));
  const nav = await chromium.launch({executablePath:'/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'});

  for (const [etq, ruta] of [['tablet nueva', ''], ['tablet vieja (Safari 12)', '?viejo=1&']]){
    console.log(`\n— ${etq} —`);
    const ctx = await nav.newContext({viewport:{width:1024, height:768}, hasTouch:true});
    const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(String(e)));
    await p.goto(`http://localhost:${PUERTO}/autoservicio.html?${ruta}sede=el-tesoro`);
    await p.waitForTimeout(1500);
    if (!(await p.evaluate(() => document.querySelector('#llave').hidden))){
      await p.fill('#l-correo','jhotas96@gmail.com');
      await p.fill('#l-clave','TzEi4LntP6I8TC');
      await p.click('#l-abrir'); await p.waitForTimeout(2500);
    }
    /* el tope de intentos es de verdad: si la corrida anterior lo gastó, se
       espera en vez de darle la vuelta */
    if (/Demasiados intentos/i.test(await p.evaluate(() => document.body.innerText))){
      console.log('     (tope de intentos gastado: espero 62 s)');
      await p.waitForTimeout(62000);
      await p.click('#l-abrir'); await p.waitForTimeout(2500);
    }
    try { await p.waitForSelector('#bienvenida:not([hidden])', {timeout: 15000}); }
    catch(e){ t('la tablet abre', false, await p.evaluate(() => document.body.innerText)); await ctx.close(); continue; }
    /* se recorre hasta una pantalla con de todo: botones, campos y avisos */
    const pantallas = [];
    const mide = async (nombre) => {
      const m = await p.evaluate(MEDIR);
      pantallas.push([nombre, m]);
    };
    await mide('inicio');
    await p.click('#bienvenida'); await p.waitForTimeout(600);
    await mide('documento');
    for (const d of '999000555')
      await p.locator('.teclas button', {hasText:new RegExp('^'+d+'$')}).first().click();
    await p.locator('button', {hasText:'Continuar'}).first().click();
    await p.waitForTimeout(2000);
    await mide('registro');
    await p.evaluate(() => { S.error = "Esa hora se acabó de ocupar. Estas son las que quedan."; pintar(); });
    await p.waitForTimeout(300);
    await mide('con un aviso de error');

    const chicos = [...new Set(pantallas.flatMap(([n,m]) => m.chicos.map(c => n + ': ' + c)))];
    t('todo botón y campo mide 44px o más', chicos.length === 0, chicos.join(' | '));

    const flojos = [];
    for (const [n, m] of pantallas)
      for (const b of m.bajos){
        const r = razon(b.color, b.fondo);
        if (r < b.minimo) flojos.push(`${n}: «${b.txt}» ${r.toFixed(2)}:1 (pide ${b.minimo})`);
      }
    t('ningún texto con poco contraste', flojos.length === 0, [...new Set(flojos)].join('\n       '));

    const avisoOk = await p.evaluate(() => {
      const a = document.querySelector('.aviso'); if (!a) return null;
      const cs = getComputedStyle(a);
      return {fondo: cs.backgroundColor, borde: cs.borderTopColor, color: cs.color};
    });
    t('el aviso de error tiene fondo propio, no se pierde sobre el vidrio',
      avisoOk && (avisoOk.fondo.match(/[\d.]+/g)||[])[3] !== '0'
        && avisoOk.fondo !== 'rgba(0, 0, 0, 0)', JSON.stringify(avisoOk));

    t('sin errores de JavaScript', errs.length === 0, errs.join('\n'));
    await p.screenshot({path:`/tmp/tablet-${etq.indexOf('vieja')>=0?'vieja':'nueva'}.png`});
    await ctx.close();
  }
  await nav.close(); srv.close();
  console.log(`\n${ok} ok, ${mal} mal`);
  process.exit(mal ? 1 : 0);
})();
