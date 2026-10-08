#!/usr/bin/env python3
"""El informe «Indicadores» de la agenda:
  1) Filtro por RANGO de fechas (desde/hasta + Este mes / Mes pasado / Todo).
  2) Un panel de PEPE que siempre dice cuantas agendo y en que estado.
Antes solo se podia ver un mes, y lo que Pepe agendo en otro mes no aparecia.
"""
import io, re, shutil, subprocess, sys

AG = "/var/www/html/agenda.html"
raw = open(AG, "rb").read()

P = []

# ── 1. el rango: etiqueta y llave del cache ──────────────────────────────
P.append((
'''  const hoy=ymd(new Date());
  const mes=S.mes;
  const act=S.sedes.filter(s=>s.activo!==false);
  titulo(top,"Indicadores",
    (S.sedeInd?((byId(S.sedes,S.sedeInd)||{}).nombre+" · "):"Todas las sedes · ")+
      MESES[+mes.slice(5,7)-1]+" "+mes.slice(0,4),''',
'''  const hoy=ymd(new Date());
  const mes=S.mes;
  /* Filtro por fechas: si hay «desde» y «hasta» manda el rango; si no, el mes
     del selector. Antes solo se podia ver UN mes, y lo que Pepe habia agendado
     en otro mes no aparecia por ningun lado. */
  const enRango=!!(S.desde&&S.hasta);
  const llave=enRango?(S.desde+"|"+S.hasta):mes;
  const bonito=f=>{const p=String(f).split("-");return (+p[2])+" "+MESES[+p[1]-1].slice(0,3)+" "+p[0];};
  const etiqueta=enRango?("del "+bonito(S.desde)+" al "+bonito(S.hasta))
                        :(MESES[+mes.slice(5,7)-1]+" "+mes.slice(0,4));
  const act=S.sedes.filter(s=>s.activo!==false);
  titulo(top,"Indicadores",
    (S.sedeInd?((byId(S.sedes,S.sedeInd)||{}).nombre+" · "):"Todas las sedes · ")+
      etiqueta,''',
"etiqueta del periodo"))

# ── 2. el selector de mes limpia el rango ────────────────────────────────
P.append((
'''      onchange:e=>{if(e.target.value){S.mes=e.target.value;cargarMes();}}}),''',
'''      onchange:e=>{if(e.target.value){S.mes=e.target.value;S.desde=S.hasta="";cargarMes();}}}),''',
"el mes limpia el rango"))

# ── 3. Actualizar: borra la llave correcta ───────────────────────────────
P.append((
'''    h("button",{class:"btn",onclick:()=>{delete S.rango[S.mes];cargarMes();}},
      svg('<path d="M20 11a8 8 0 1 0-2.3 5.7"/><path d="M20 5v6h-6"/>'),"Actualizar"),''',
'''    h("button",{class:"btn",onclick:()=>{delete S.rango[llave];delete S.rango[S.mes];cargarMes();}},
      svg('<path d="M20 11a8 8 0 1 0-2.3 5.7"/><path d="M20 5v6h-6"/>'),"Actualizar"),''',
"Actualizar borra la llave del rango"))

# ── 4. exportar con la llave del rango ───────────────────────────────────
P.append((
'''    btnExportar(()=>(S.rango[S.mes]||[]).filter(c=>c.tipo!=="bloqueo"&&(!S.sedeInd||c.sedeId===S.sedeInd)),
      ()=>"citas-"+S.mes+''',
'''    btnExportar(()=>(S.rango[llave]||[]).filter(c=>c.tipo!=="bloqueo"&&(!S.sedeInd||c.sedeId===S.sedeInd)),
      ()=>"citas-"+llave.replace("|","_a_")+''',
"exportar con la llave del rango"))

# ── 5. esperar la llave, no el mes ───────────────────────────────────────
P.append((
'''  if(!S.rango[mes]){ cargarMes();
    view.appendChild(h("div",{class:"g empty"},h("h3",null,"Calculando…"),h("p",null,"Estoy leyendo las citas del mes.")));
    return;
  }
  const citas=S.rango[mes].filter(c=>c.tipo!=="bloqueo"&&(!S.sedeInd||c.sedeId===S.sedeInd));''',
'''  if(!S.rango[llave]){ cargarMes();
    view.appendChild(h("div",{class:"g empty"},h("h3",null,"Calculando…"),h("p",null,"Estoy leyendo las citas del período.")));
    return;
  }
  const citas=S.rango[llave].filter(c=>c.tipo!=="bloqueo"&&(!S.sedeInd||c.sedeId===S.sedeInd));''',
"esperar la llave del rango"))

# ── 6. la capacidad se prorratea por los dias del rango ──────────────────
P.append((
'''  const capMes=(S.sedeInd?act.filter(s=>s.id===S.sedeInd):act)
    .reduce((a,s)=>a+(s.puestos||0)*(s.capacidadDia||16)*(s.diasMes||24),0);''',
'''  /* Los cupos del mes; si se filtra por un rango, se prorratean por sus dias. */
  const diasPeriodo=enRango?Math.max(1,Math.round((new Date(S.hasta)-new Date(S.desde))/86400000)+1):30;
  const capMes=Math.round((S.sedeInd?act.filter(s=>s.id===S.sedeInd):act)
    .reduce((a,s)=>a+(s.puestos||0)*(s.capacidadDia||16)*(s.diasMes||24)*(diasPeriodo/30),0));''',
"capacidad prorrateada"))

# ── 7. la barra de fechas ────────────────────────────────────────────────
P.append((
'''  view.appendChild(h("div",{class:"kpis"},
    kpi("% Agendamiento",''',
'''  /* Barra de fechas: el informe se puede mirar por un rango, no solo por mes. */
  view.appendChild(h("div",{class:"g pad",style:{marginTop:"11px",display:"flex",gap:"10px",alignItems:"flex-end",flexWrap:"wrap"}},
    h("label",{style:{display:"flex",flexDirection:"column",gap:"4px"}},
      h("span",{class:"muted"},"Desde"),
      h("input",{type:"date",value:S.desde||"",style:{maxWidth:"165px"},
        onchange:e=>{S.desde=e.target.value;if(S.desde&&S.hasta)cargarMes();}})),
    h("label",{style:{display:"flex",flexDirection:"column",gap:"4px"}},
      h("span",{class:"muted"},"Hasta"),
      h("input",{type:"date",value:S.hasta||"",style:{maxWidth:"165px"},
        onchange:e=>{S.hasta=e.target.value;if(S.desde&&S.hasta)cargarMes();}})),
    h("button",{class:"btn",onclick:()=>{const d=new Date();
      S.desde=ymd(new Date(d.getFullYear(),d.getMonth(),1));
      S.hasta=ymd(new Date(d.getFullYear(),d.getMonth()+1,0));cargarMes();}},"Este mes"),
    h("button",{class:"btn",onclick:()=>{const d=new Date();
      S.desde=ymd(new Date(d.getFullYear(),d.getMonth()-1,1));
      S.hasta=ymd(new Date(d.getFullYear(),d.getMonth(),0));cargarMes();}},"Mes pasado"),
    h("button",{class:"btn",onclick:()=>{S.desde="2020-01-01";S.hasta=ymd(new Date());cargarMes();}},"Todo"),
    h("button",{class:"btn",onclick:()=>{S.desde=S.hasta="";delete S.rango[S.mes];cargarMes();}},"Limpiar filtro")),
  view.appendChild(h("div",{class:"kpis"},
    kpi("% Agendamiento",''',
"la barra de fechas"))

# ── 8. textos: del mes -> del periodo ────────────────────────────────────
for viejo, nuevo, etq in (
    ('" de "+nf(capMes)+" cupos del mes"', '" de "+nf(capMes)+" cupos del período"', "cupos del periodo"),
    ('kpi("Citas del mes"', 'kpi(enRango?"Citas del período":"Citas del mes"', "citas del periodo"),
    ('"Sin citas este mes."', '"Sin citas en este período."', "sin citas"),
    ('"Top 12 del mes"', '"Top 12 del período"', "top 12"),
    ('"Citas agendadas contra la capacidad del mes"', '"Citas agendadas contra la capacidad del período"', "capacidad"),
    ('"Productividad por persona en el mes"', '"Productividad por persona en el período"', "productividad"),
    ('"Todavía no hay citas registradas este mes."', '"Todavía no hay citas registradas en este período."', "todavia no hay"),
):
    P.append((viejo, nuevo, etq))

# ── 9. el panel de Pepe ──────────────────────────────────────────────────
P.append((
'''  resolverPerfiles(Object.keys(porUsuario).filter(k=>/^u[-_]/.test(k)));''',
'''  /* Pepe, siempre a la vista: cuantas agendo y en que estado. */
  const dePepe=citas.filter(c=>c.canal==="Agente IA"||/pepe/i.test(String(c.asignadaPor||"")));
  const estPepe={};
  dePepe.forEach(c=>{const e=estadoDe(c.estadoId)||{};const n=e.nombre||"—";estPepe[n]=(estPepe[n]||0)+1;});
  view.appendChild(h("div",{style:{marginTop:"13px"}},
    panel("Pepe · agente IA","Cuántas citas ha agendado y en qué estado",
      dePepe.length
        ? h("div",null,
            h("div",{style:{fontSize:"26px",fontWeight:"700",marginBottom:"9px"}},nf(dePepe.length)+" agendadas"),
            barras(Object.keys(estPepe).map(k=>({t:k,v:estPepe[k]})),dePepe.length))
        : h("p",{class:"muted"},"Pepe no agendó nada en este período."))));

  resolverPerfiles(Object.keys(porUsuario).filter(k=>/^u[-_]/.test(k)));''',
"el panel de Pepe"))

# ── 10. cargarMes entiende el rango ──────────────────────────────────────
P.append((
'''async function cargarMes(o){
  o=o||{};
  const mes=S.mes;
  try{
    /* Ojo: no todos los meses tienen 31 dias. Pidiendo "-31" en
       septiembre la API devolvia error y el reporte caia al cache del
       dia, que no sabe quien agendo la cita. */
    const ult=String(new Date(+mes.slice(0,4),+mes.slice(5,7),0).getDate()).padStart(2,"0");
    const snap=await S.db.collection("citas").where("fecha",">=",mes+"-01").where("fecha","<=",mes+"-"+ult).limit(400).get();
    const out=[];
    snap.docs.forEach(d=>{ const it=d.data().items||{}; Object.values(it).forEach(c=>out.push(c)); });
    S.rango[mes]=out; render();
  }catch(e){
    /* Callada (el reloj): se deja lo que había y no se molesta a nadie con un
       aviso. Un parpadeo de red no puede vaciarle el reporte en la cara a
       quien lo está leyendo. */
    if(o.silencioso){ console.warn("mes", e&&e.message); return; }
    S.rango[mes]=[]; toast("No se pudieron leer las citas del mes.",true); render();
  }
}''',
'''async function cargarMes(o){
  o=o||{};
  const mes=S.mes;
  const enRango=!!(S.desde&&S.hasta);
  const llave=enRango?(S.desde+"|"+S.hasta):mes;
  /* Ojo: no todos los meses tienen 31 dias. Pidiendo "-31" en septiembre la
     API devolvia error y el reporte caia al cache del dia, que no sabe quien
     agendo la cita. */
  const desde=enRango?S.desde:(mes+"-01");
  const hasta=enRango?S.hasta:(mes+"-"+String(new Date(+mes.slice(0,4),+mes.slice(5,7),0).getDate()).padStart(2,"0"));
  try{
    const snap=await S.db.collection("citas").where("fecha",">=",desde).where("fecha","<=",hasta).limit(2000).get();
    const out=[];
    snap.docs.forEach(d=>{ const it=d.data().items||{}; Object.values(it).forEach(c=>out.push(c)); });
    S.rango[llave]=out; render();
  }catch(e){
    /* Callada (el reloj): se deja lo que había y no se molesta a nadie con un
       aviso. Un parpadeo de red no puede vaciarle el reporte en la cara a
       quien lo está leyendo. */
    if(o.silencioso){ console.warn("rango", e&&e.message); return; }
    S.rango[llave]=[]; toast("No se pudieron leer las citas del período.",true); render();
  }
}''',
"cargarMes entiende el rango"))

# ═══════════════════════════ aplicar ═════════════════════════════════════
shutil.copy2(AG, AG + ".pre-rango-fechas.bak")
print("respaldo:", AG + ".pre-rango-fechas.bak")
for viejo, nuevo, etq in P:
    vb, nb = viejo.encode("utf-8"), nuevo.encode("utf-8")
    n = raw.count(vb)
    print("   %-42s %s" % (etq, "1 ok" if n == 1 else "ABORTO: %d" % n))
    if n != 1:
        sys.exit(1)
    raw = raw.replace(vb, nb)
open(AG, "wb").write(raw)
print("\nescrito. bytes:", len(raw))

# ═══════════════════════════ verificar ═══════════════════════════════════
h = io.open(AG, encoding="utf-8", errors="replace").read()
bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", h, re.S | re.I)
io.open("/tmp/chk_rango.js", "w", encoding="utf-8").write("\n;\n".join(bloques))
r = subprocess.run(["node", "--check", "/tmp/chk_rango.js"], capture_output=True, text=True)
print("JS de la agenda:", "OK" if r.returncode == 0 else "MAL\n" + r.stderr[-500:])
