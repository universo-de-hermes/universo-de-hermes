/* Fuerza el estado "se venció el cupo" y comprueba que el panel diga la VERDAD. */
const {chromium} = require('playwright');
const http = require('http'), fs = require('fs');
const PAGINA = '/var/www/html/autoservicio.html', PUERTO = 8981, API = 8001;
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
  await p.goto(`http://localhost:${PUERTO}/autoservicio.html?sede=el-tesoro`);
  await p.waitForTimeout(2500);

  /* La tablet pide el usuario de recepcion UNA vez por aparato: aqui se
     entra como lo haria recepcion, para poder ver las pantallas de verdad. */
  const inputs = await p.$$("#vista input");
  if (inputs.length >= 2){
    await inputs[0].fill('jhotas96@gmail.com');
    await inputs[1].fill('TzEi4LntP6I8TC');
    for (const bt of await p.$$("#vista button")){
      if ((await bt.innerText()).trim().toLowerCase() === "abrir"){ await bt.click(); break; }
    }
    await p.waitForTimeout(2500);
    console.log("(entro como recepcion)");
  }

  const r = await p.evaluate(() => {
    /* Situacion: la clienta ya llego al resumen, pero se le vencio el tiempo */
    S.servicio = {id:"srv-1-sesion-zona-l", nombre:"1 Sesión Zona L"};
    S.fechaLarga = "viernes 2 de octubre de 2026";
    S.hora = "09:00"; S.fecha = "2026-10-02";
    S.especialista = {id:"e", nombre:"Valentina Baquero Rivillas"};
    S.cliente = {nombre:"Prueba"};
    S.modo = "agendar"; S.cupoVencido = true; S.segundos = 0;
    S.reserva = null; ir("resumen");
    /* La tarjeta de "Abrir esta tablet" vive fuera de #vista y tapa la
       pantalla: se oculta solo para la foto. */
    ["#bienvenida", "#modal", "#llave"].forEach(function(s){
      var e = document.querySelector(s); if (e) e.hidden = true; });
    Array.prototype.forEach.call(document.querySelectorAll(".caja"), function(e){
      if ((e.innerText || "").indexOf("Abrir esta tablet") >= 0) e.hidden = true; });
    var textos = [], botones = [];
    document.querySelectorAll("#vista .aviso").forEach(function(a){ textos.push(a.innerText.trim()); });
    document.querySelectorAll("#vista .fila button").forEach(function(x){ botones.push(x.innerText.trim()); });
    return {avisos:textos, botones:botones,
            reloj: !!document.querySelector("#cupo-reloj")};
  });
  console.log("avisos que ve la clienta:", JSON.stringify(r.avisos, null, 1));
  console.log("botones:", r.botones);
  console.log("(con el cupo vencido NO debe haber contador):", r.reloj ? "SI HAY (malo)" : "no hay (bien)");
  await p.screenshot({path:'/tmp/pant-vencido.png'});

  /* y ahora el estado normal: el contador debe existir */
  const r2 = await p.evaluate(() => {
    S.cupoVencido = false; S.segundos = 118; ir("resumen");
    arrancarRelojCupo();
    return {reloj: (document.querySelector("#cupo-reloj")||{}).innerText || "",
            botones: Array.prototype.map.call(document.querySelectorAll("#vista .fila button"),
                                              function(x){ return x.innerText.trim(); })};
  });
  console.log("\ncon el cupo vivo -> contador:", JSON.stringify(r2.reloj), "| botones:", r2.botones);
  await p.waitForTimeout(1200);
  const r3 = await p.evaluate(() => (document.querySelector("#cupo-reloj")||{}).innerText || "");
  console.log("un segundo despues el contador dice:", JSON.stringify(r3), "(debe haber bajado)");
  console.log("\nERRORES DE JS:", errores.length ? errores : "ninguno");
  await b.close(); srv.close();
})();
