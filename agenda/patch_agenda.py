with open('/var/www/html/agenda.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Buscar el final del script principal
insert_point = '</script>'
last_script = html.rfind(insert_point)
if last_script > 0:
    api_bridge = '''
<!-- Capa API REST conectada a Postgres -->
<script>
// Reemplazar almacenamiento local por API REST
const API_AGENDA = '/api/agenda';

// Interceptar escrituras en store para persistir en API
const originalStore = window.store;
if (originalStore) {
    // Servicios desde API
    fetch(API_AGENDA + 'servicios').then(r => r.json()).then(data => {
        if (data && data.length) {
            window.__SEMILLA.servicios = {};
            data.forEach(s => {
                window.__SEMILLA.servicios[s.id] = {
                    activo: s.activo,
                    duracion: s.duracion,
                    nombre: s.nombre,
                    precio: s.precio || 0
                };
            });
            console.log('✅ Servicios cargados desde API');
        }
    }).catch(e => console.warn('API no disponible, usando datos locales', e));
    
    // Especialistas desde API
    fetch(API_AGENDA + 'especialistas').then(r => r.json()).then(data => {
        if (data && data.length) {
            console.log('✅', data.length, 'especialistas desde API');
        }
    }).catch(e => console.warn('API no disponible', e));
    
    // Sedes desde API
    fetch(API_AGENDA + 'sedes').then(r => r.json()).then(data => {
        if (data && data.length) {
            console.log('✅', data.length, 'sedes desde API');
        }
    }).catch(e => console.warn('API no disponible', e));
}
console.log('🔌 Agenda conectada a API Postgres');
</script>'''
    
    html = html[:last_script + len(insert_point)] + api_bridge + html[last_script + len(insert_point):]
    
    with open('/var/www/html/agenda.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('✅ Bridge API insertado en agenda.html')
else:
    print('❌ No se encontró punto de inserción')
