/* Guardado como prueba fija: se corre con  node probar-ios9.js  */
/* Simula iOS 9: se borran fetch, URLSearchParams, sendBeacon y el CSS
   moderno ANTES de que corra la página, y se recorre el agendamiento
   completo contra la agenda de verdad. Si aquí agenda, en el iPad agenda. */
const {chromium}=require('playwright');const http=require('http'),fs=require('fs');
const {execSync}=require('child_process');
const PU=8960, API=8001, DOC='999000444', TEL='3009998877';
let ok=0,mal=0;
const t=(n,c,e)=>{if(c){ok++;console.log('  ok   '+n);}else{mal++;console.log('  MAL  '+n+(e?'\n       '+String(e).slice(0,300):''));}};
let html=fs.readFileSync('/var/www/html/autoservicio.html','utf8');
html=html.replace(/[a-z-]+:[^;{}]*clamp\([^;{}]*\)[^;{}]*;/g,'')
         .replace(/[a-z-]+:[^;{}]*color-mix\([^;{}]*\)[^;{}]*;/g,'')
         .replace(/display:grid;/g,'').replace(/grid-template-rows:[^;{}]*;?/g,'')
         .replace(/grid-row:\d+;/g,'').replace(/row-gap:[^;{}]*;?/g,'')
         .replace(/justify-items:[^;{}]*;?/g,'').replace(/text-wrap:[^;{}]*;?/g,'');
const srv=http.createServer((q,r)=>{
  if(q.url.startsWith('/api/')){
    const x=http.request({host:'127.0.0.1',port:API,path:q.url.slice(4),method:q.method,headers:q.headers},
      y=>{r.writeHead(y.statusCode,y.headers);y.pipe(r);});
    x.on('error',()=>{r.writeHead(502);r.end('{}')});q.pipe(x);return;}
  r.writeHead(200,{'content-type':'text/html; charset=utf-8'});r.end(html);});
(async()=>{
  try{execSync(`python3 /home/claude/limpiar-prueba.py ${DOC}`,{stdio:'ignore'});}catch(e){}
  await new Promise(r=>srv.listen(PU,r));
  const nav=await chromium.launch({executablePath:'/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'});
  const ctx=await nav.newContext({viewport:{width:768,height:1024},hasTouch:true});
  /* esto es lo que hace que sea iOS 9 */
  await ctx.addInitScript(()=>{
    delete window.fetch; delete window.URLSearchParams;
    try{ delete navigator.sendBeacon; }catch(e){}
    Object.defineProperty(navigator,'sendBeacon',{get(){return undefined;},configurable:true});
  });
  const p=await ctx.newPage(); const errs=[];
  p.on('pageerror',e=>errs.push(String(e)));
  const texto=()=>p.evaluate(()=>document.body.innerText);
  const toca=async s=>p.locator('button',{hasText:s}).first().click();
  const digitar=async n=>{for(const d of String(n))
    await p.locator('.teclas button',{hasText:new RegExp('^'+d+'$')}).first().click();};

  await p.goto(`http://localhost:${PU}/autoservicio.html?sede=el-tesoro`);
  await p.waitForTimeout(1500);
  t('sin fetch ni URLSearchParams, la página igual arranca',
    await p.evaluate(()=>!document.querySelector('#llave').hidden
      || !document.querySelector('#bienvenida').hidden), await texto());
  t('y leyó la sede de la dirección, sin URLSearchParams',
    await p.evaluate(()=>SEDE==='el-tesoro'));
  if(!(await p.evaluate(()=>document.querySelector('#llave').hidden))){
    await p.fill('#l-correo','jhotas96@gmail.com');
    await p.fill('#l-clave','TzEi4LntP6I8TC');
    await p.click('#l-abrir'); await p.waitForTimeout(2500);
  }
  t('recepción puede abrir la tablet (eso es un POST con el fetch de repuesto)',
    await p.evaluate(()=>document.querySelector('#llave').hidden), await texto());
  await p.click('#bienvenida'); await p.waitForTimeout(700);
  await digitar(DOC); await toca('Continuar'); await p.waitForTimeout(2000);
  t('busca la cédula contra la agenda', /Cuéntenos quién es|Hola,/i.test(await texto()), await texto());
  const campo=async(ph,v)=>p.locator(`input[placeholder="${ph}"]`).first().fill(v);
  await campo('Escriba su nombre','Prueba'); await campo('Escriba su apellido','iOS9');
  await campo('Escriba su celular',TEL); await campo('Escriba su correo','ios9@cjmedical.co');
  await toca('Guardar y continuar'); await p.waitForTimeout(2500);
  t('la registra y llega a los servicios', /Escoja el servicio/i.test(await texto()), await texto());
  await p.locator('.opcion').first().click(); await p.waitForTimeout(900);
  await toca('Otro día'); await p.waitForTimeout(900);
  let hay=false;
  for(let i=0;i<10&&!hay;i++){
    const libres=await p.$$('.cal .dias button:not([disabled])');
    if(!libres.length){await p.locator('.cal .cab button').last().click();
                       await p.waitForTimeout(400);continue;}
    await libres[Math.min(i,libres.length-1)].click();
    await p.waitForTimeout(1800);
    hay=/Escoja la hora/i.test(await texto()) && (await p.$$('.hora')).length>0;
    if(!hay && /no quedan horas/i.test(await texto())){
      await toca('Ver otro día'); await p.waitForTimeout(700);}
  }
  t('le muestra horas libres de verdad', hay, await texto());
  await p.locator('.hora').first().click(); await p.waitForTimeout(2000);
  /* El panel NO pregunta cuando a esa hora hay una sola especialista:
     pasa derecho al resumen. Asi que solo se toca la ficha si esa pantalla salio. */
  if (/Escoja con quién/i.test(await texto())){
    await p.locator('.opcion').first().click(); await p.waitForTimeout(2000);
  }
  t('llega al resumen', /Revise su cita/i.test(await texto()), await texto());
  await toca('Confirmar cita'); await p.waitForTimeout(3000);
  t('y AGENDA la cita, en un navegador sin fetch',
    /Listo/i.test(await texto()) && /LLEG|CONFIRMAD|PENDIENTE/i.test(await texto()), await texto());
  t('sin errores de JavaScript', errs.length===0, errs.join('\n'));
  try{execSync(`python3 /home/claude/limpiar-prueba.py ${DOC}`,{stdio:'ignore'});}catch(e){}
  await p.screenshot({path:'/tmp/ios9-final.png'});
  await nav.close();srv.close();
  console.log(`\n${ok} ok, ${mal} mal`);
  process.exit(mal?1:0);
})();
