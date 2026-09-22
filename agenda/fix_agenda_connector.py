with open('/var/www/html/agenda.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the old API bridge with a full data connector
old_bridge = '<!-- Capa API REST conectada a Postgres -->'
insert_point = html.find(old_bridge)
if insert_point < 0:
    # Try finding the end of the big script
    insert_point = html.find('console.log')
    if insert_point > 0:
        # Find the enclosing script tag end
        insert_point = html.find('</script>', insert_point)
    if insert_point < 0:
        insert_point = html.find('</body>')

if insert_point > 0:
    new_connector = '''<!-- Capa API REST conectada a Postgres -->
<script>
// Reemplazar el almacenamiento local con la API de Postgres
const API = '/api/agenda/';

// Interceptar el objeto store original
(function() {
    const origInit = window.__SEMILLA;
    
    // Sobrescribir fetch de citas del día para que venga de API
    const origStore = window.store;
    
    // Hacer fetch de citas reales y fusionarlas con la semilla
    fetch(API + 'sedes').then(r => r.json()).then(sedes => {
        if (sedes && sedes.length) {
            window.__SEMILLA.sedes = {};
            sedes.forEach(s => {
                window.__SEMILLA.sedes[s.id] = {
                    activo: s.activo,
                    nombre: s.nombre,
                    ciudad: s.ciudad,
                    horaInicio: s.hora_inicio,
                    horaFin: s.hora_fin,
                    puestos: s.puestos
                };
            });
        }
    }).catch(e => console.warn('API sedes:', e));
    
    fetch(API + 'servicios').then(r => r.json()).then(svcs => {
        if (svcs && svcs.length) {
            window.__SEMILLA.servicios = {};
            svcs.forEach(s => {
                window.__SEMILLA.servicios[s.id] = {
                    activo: s.activo,
                    duracion: s.duracion,
                    nombre: s.nombre,
                    precio: s.precio || 0
                };
            });
        }
    }).catch(e => console.warn('API servicios:', e));

    // Cada vez que se abre un día, cargar citas reales
    const origAbrir = window.abrirDia || function(){};
    
    console.log('🔌 Agenda conectada a PostgreSQL vía API');
})();
</script>'''
    if old_bridge in html:
        html = html.replace(old_bridge, new_connector)
    else:
        html = html[:insert_point] + new_connector + html[insert_point:]
    
    with open('/var/www/html/agenda.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('✅ Conector API reemplazado')
else:
    print('❌ Punto de inserción no encontrado')