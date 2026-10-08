/* Abre el panel como una clienta y dice que se ve al arrancar, con los errores. */
const {chromium} = require('playwright');
const http = require('http'), fs = require('fs');
const PAGINA = '/var/www/html/autoservicio.html', PUERTO = 8979, API = 8001;
const srv = http.createServer((q,r) => {
  if (q.url.startsWith('/api/')){
    const x = http.request({host:'127.0.0.1', port:API, path:q.url.slice(4),
      method:q.method, headers:q.headers}, y => { r.writeHead(y.statusCode,y.headers); y.pipe(r); });
    x.on('error', () => { r.writeHead(502); r.end('{}'); }); q.pipe(x); return;
  }
  fs.readFile(PAGINA,(e,b) => { r.writeHead(200,{'content-type':'text/html; charset=utf-8'}); r.end(b); });
});
(async () => {
  await new Promise(res => srv.listen(PUERTO, res));
  const b = await chromium.launch({executablePath:'/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'});
  const p = await b.newPage({viewport:{width:1024,height:768}});
  const errores = [];
  p.on('pageerror', e => errores.push('PAGEERROR: ' + e.message));
  p.on('console', m => { if (m.type()==='error') errores.push('CONSOLA: ' + m.text()); });
  await p.goto(`http://localhost:${PUERTO}/autoservicio.html?sede=el-tesoro`);
  await p.waitForTimeout(4000);
  const estado = await p.evaluate(() => ({
    bienvenida: document.querySelector('#bienvenida') ? !document.querySelector('#bienvenida').hidden : 'no existe',
    texto: (document.body.innerText || '').replace(/\s+/g,' ').slice(0,240),
    vista: document.querySelector('#vista') ? document.querySelector('#vista').innerText.slice(0,160) : ''
  }));
  console.log('bienvenida visible:', estado.bienvenida);
  console.log('texto de la pagina:', estado.texto);
  console.log('vista:', estado.vista);
  console.log('ERRORES DE JS:', errores.length ? errores.slice(0,6) : 'ninguno');
  await p.screenshot({path:'/tmp/panel-arranque.png'});
  await b.close(); srv.close();
})();
