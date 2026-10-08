/* Comprueba en el navegador los cambios d) y e), y el orden de los servicios. */
const {chromium} = require('playwright');
const http = require('http'), fs = require('fs');
const PAGINA = '/var/www/html/autoservicio.html', PUERTO = 8985, API = 8001;
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

  const r = await p.evaluate(() => {
    const salida = {};
    /* d) la pantalla "usted ya tiene una cita" */
    S.citaPrevia = {cuando:"hoy", servicio:"1 Sesión Zona L",
                    fecha_larga:"viernes 2 de octubre de 2026", hora_larga:"9:00 a. m.",
                    especialista:"Valentina Baquero", estado:"Confirmado", es_hoy:true,
                    id:"x", servicio_id:"s"};
    S.puedeCambiar = true; S.mensajeLimite = "";
    ir("cita");
    salida.cita_titulo = (document.querySelector("#vista h1")||{}).innerText || "";
    salida.cita_sub    = (document.querySelector("#vista .sub")||{}).innerText || "";

    /* e) el orden de las especialistas */
    S.hora = "09:00"; S.libres = [{id:"1",nombre:"Valentina Baquero Rivillas"},
                                  {id:"2",nombre:"Julie Arias Hernández"}];
    S.horas = [{hora:"09:00", hora_larga:"9:00 a. m."}];
    S.fechaLarga = "sábado 3 de octubre de 2026";
    ir("especialista");
    salida.especialistas = Array.prototype.map.call(
      document.querySelectorAll("#vista .opcion .t"), function(e){ return e.innerText.trim(); });

    /* c) el orden de los servicios que le llegan */
    salida.servicios = ((D && D.servicios) || []).slice(0, 6).map(function(s){
      return s.nombre + " (" + s.duracion + "m)"; });
    salida.total_servicios = ((D && D.servicios) || []).length;
    return salida;
  });

  console.log("=== d) pantalla «ya tiene una cita» ===");
  console.log("   título : " + JSON.stringify(r.cita_titulo));
  console.log("   subtítulo: " + JSON.stringify(r.cita_sub));
  console.log("\n=== e) orden de las especialistas ===");
  console.log("   " + JSON.stringify(r.especialistas));
  console.log("   (los nombres primero, «Me da igual» al final)");
  console.log("\n=== c) los primeros servicios que ve la clienta ===");
  console.log("   total: " + r.total_servicios);
  r.servicios.forEach(function(s, i){ console.log("   " + (i+1) + ". " + s); });
  console.log("\nERRORES DE JS:", errores.length ? errores : "ninguno");
  await b.close(); srv.close();
})();
