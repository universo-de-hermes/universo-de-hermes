import re

with open('/var/www/html/agenda.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find window.__SEMILLA = { ... };
match = re.search(r'window\.__SEMILLA\s*=\s*\{', html)
if not match:
    print("ERROR: No se encontró window.__SEMILLA")
    exit(1)

start = match.start()
# Find the corresponding closing of the entire SEMILLA + initialization
# We need to find where the seed data ends and the page rendering begins
# The pattern is: ...citadatos}}};\n(function(){
target = '};\n(function(){'
end = html.find(target, start + 50)
if end < 0:
    # Try alternative patterns
    target = '}\n(function(){'
    end = html.find(target, start + 50)
if end < 0:
    target = '}};\n(function(){'
    end = html.find(target, start + 50)

if end < 0:
    print("ERROR: No se encontró el final del bloque SEMILLA")
    exit(1)

# Build the replacement
replacement = """window.__SEMILLA = {};
// Cargar datos reales desde la API de Postgres
(async function initAgenda() {
  try {
    let r = await fetch('/api/agenda/api/v2/datos');
    let d = await r.json();
    if (d) {
      window.__SEMILLA = {
        config: { app: { nombre: 'CJ Medical', sedeDefault: 'sede-cj-medical-el-tesoro', slot: 30, zoom: 1.5 } },
        sedes: d.sedes || {},
        servicios: d.servicios || {},
        estados: d.estados || {},
        especialistas: d.especialistas || {},
        citas: {},
        usuarios: {},
        pendientes: {}
      };
      console.log('✅ Agenda conectada a PostgreSQL -', Object.keys(d.sedes).length, 'sedes,', Object.keys(d.servicios).length, 'servicios');
    }
  } catch(e) { console.warn('⚠️ API no disponible, usando datos de respaldo', e); }
  // Inicializar la interfaz
  var P = new URLSearchParams(location.search);
  var BD = "cjm-agenda", TIENDA = "docs", CLAVE_LS = "cjm-agenda-datos";
  var store = {};
  var subs = [];
  var idb = null;
  var modo = "memoria";"""

html = html[:start] + replacement + html[end + len(target):]

# Also need to add citas loading when a day is selected
# Find the function that renders the day
# Add citas loading before the main init
day_fn = html.find('function abrirDia')
if day_fn > 0:
    # Add API call before abrirDia
    api_citas = """
// Al cambiar de fecha, cargar citas desde la API
var cargarCitasAPI = async function(fecha, sedeId) {
  try {
    let r = await fetch('/api/agenda/api/v2/agenda/' + sedeId + '/' + fecha);
    let d = await r.json();
    if (d && d.length) {
      if (!window.__SEMILLA.citas) window.__SEMILLA.citas = {};
      if (!window.__SEMILLA.citas[fecha]) window.__SEMILLA.citas[fecha] = { fecha: fecha, items: {} };
      d.forEach(function(c) {
        window.__SEMILLA.citas[fecha].items[c.id] = {
          clienteId: c.cliente_id, especialistaId: c.especialista_id,
          estadoId: c.estado_id, fecha: fecha,
          fin: c.fin || '', id: c.id,
          inicio: c.inicio.substring(0,5),
          sedeId: c.sede_id, servicioId: c.servicio_id, tipo: 'cita',
          clienteNombre: c.cliente_nombre, especialistaNombre: c.especialista_nombre,
          servicioNombre: c.servicio_nombre
        };
      });
    }
  } catch(e) { console.warn('Citas API:', e); }
};

"""
    html = html[:day_fn] + api_citas + html[day_fn:]

with open('/var/www/html/agenda.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ HTML parcheado - conectado a PostgreSQL")
print(f"Bloque SEMILLA reemplazado (posición {start}-{end})")
print(f"Función cargarCitasAPI insertada antes de abrirDia")