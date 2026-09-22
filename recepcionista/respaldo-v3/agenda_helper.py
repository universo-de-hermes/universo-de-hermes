"""
Helper de agenda CJ Medical para Pepe.
Conecta con la API REST de la agenda en Postgres.
"""
import httpx
import logging
from typing import Optional

logger = logging.getLogger(__name__)

AGENDA_API = "http://127.0.0.1:8001"

# ── Mapeo de servicios Pepe → IDs de la agenda ──
SERVICIO_MAP = {
    "terapia de revitalización": "srv-terapias-de-revitalizacion",
    "terapia": "srv-terapias-de-revitalizacion",
    "masaje relajante": "srv-masaje-de-relajacion",
    "masaje": "srv-masaje-de-relajacion",
    "carbon peel": "srv-carbon-peel",
    "carbon": "srv-carbon-peel",
    "hidrafacial básico": "srv-hidrofacial-basica",
    "hidrafacial basico": "srv-hidrofacial-basica",
    "hidrafacial plus": "srv-hidrafacial-plus",
    "hidrafacial": "srv-hidrofacial-basica",
    "casmara": None,
    "peeling químico": "srv-consulta-medica",
    "peeling": "srv-consulta-medica",
    "depilación láser zona xs": "srv-1-sesion-zona-xs",
    "depilación láser zona s": "srv-1-sesion-zona-s",
    "depilación láser zona m": "srv-1-sesion-zona-m",
    "depilación láser zona l": "srv-1-sesion-zona-l",
    "depilación láser": "srv-1-sesion-zona-m",
    "depilacion laser": "srv-1-sesion-zona-m",
    "remoción de micropigmentación": "srv-remocion-micropigmentacion-1-sesion",
    "micropigmentacion": "srv-remocion-micropigmentacion-1-sesion",
    "valoración inicial médica": "srv-consulta-medica",
    "valoracion inicial medica": "srv-consulta-medica",
    "botox": "srv-toxina-botox",
    "radiofrecuencia fraccionada": "srv-radiofrecuencia-fraccionada-alta-intensidad",
    "radiofrecuencia": "srv-radiofrecuencia-fraccionada-alta-intensidad",
    "rf fraccionada + exosomas": "srv-radiofrecuencia-fraccionada-alta-intensidad",
    "diseño de cejas": "srv-diseno-de-cejas",
    "diseno de cejas": "srv-diseno-de-cejas",
    "tintura de cejas": "srv-tintura-de-cejas",
}

SEDE_MAP = {
    "bogotá": "sede-cj-medical-bogota",
    "bogota": "sede-cj-medical-bogota",
    "chico norte": "sede-cj-medical-bogota",
    "medellín": "sede-cj-medical-el-tesoro",
    "medellin": "sede-cj-medical-el-tesoro",
    "el tesoro": "sede-cj-medical-el-tesoro",
}

def get_servicio_id(servicio: str) -> Optional[str]:
    """Convierte nombre de servicio Pepe a ID de agenda."""
    s = servicio.lower().strip()
    if s in SERVICIO_MAP:
        return SERVICIO_MAP[s]
    # Búsqueda parcial
    for key, val in SERVICIO_MAP.items():
        if key in s or s in key:
            return val
    return None

def get_sede_id(ciudad: str) -> Optional[str]:
    s = ciudad.lower().strip()
    for key, val in SEDE_MAP.items():
        if key in s or s in key:
            return val
    return None

def get_especialista_por_servicio(servicio_id: str, sede_id: str) -> Optional[str]:
    """Busca especialista disponible para un servicio en una sede."""
    # Consultar por las reglas de CJ Medical
    if servicio_id == "srv-toxina-botox":
        # Botox: Dr. Cueter en Bogotá, Dr. Cueter/Dra. Arias en Medellín
        pass
    # Por defecto, huecos_del_dia con especialista=None busca cualquiera
    return None

async def buscar_cliente(telefono: str) -> list:
    """Busca cliente por teléfono en la agenda."""
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{AGENDA_API}/clientes/buscar", json={"telefono": telefono})
        if r.status_code == 200:
            return r.json()
        return []

async def crear_cliente(documento: str, nombre: str, apellido: str, telefono: str, correo: str, sede: str) -> dict:
    """Crea un cliente en la agenda y devuelve su ID."""
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{AGENDA_API}/clientes/crear", json={
            "documento": documento,
            "primer_nombre": nombre,
            "primer_apellido": apellido,
            "telefono": telefono,
            "correo": correo,
            "sede": sede
        })
        if r.status_code == 200:
            return r.json()
        return {}

async def get_huecos(fecha: str, sede: str, servicio: str, paso: int = 15) -> list:
    """Obtiene los huecos disponibles para una fecha, sede y servicio."""
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{AGENDA_API}/huecos/dia", json={
            "fecha": fecha,
            "sede": sede,
            "servicio": servicio,
            "paso": paso
        })
        if r.status_code == 200:
            return r.json()
        return []

async def apartar_cupo(especialista: str, sede: str, fecha: str, inicio: str, servicio: str, referencia: str) -> dict:
    """Aparta un cupo por 5 minutos."""
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{AGENDA_API}/cupos/apartar", json={
            "especialista": especialista,
            "sede": sede,
            "fecha": fecha,
            "inicio": inicio,
            "servicio": servicio,
            "referencia": referencia
        })
        return r.json() if r.status_code == 200 else {}

async def agendar(cliente_id: str, especialista: str, sede: str, fecha: str, inicio: str, servicio: str,
                  canal: str = "WhatsApp", por: str = "pepe", notas: str = "", reserva: str = "") -> dict:
    """Agenda una cita definitiva."""
    payload = {
        "cliente_id": cliente_id,
        "especialista": especialista,
        "sede": sede,
        "fecha": fecha,
        "inicio": inicio,
        "servicio": servicio,
        "canal": canal,
        "por": por,
        "notas": notas,
    }
    if reserva:
        payload["reserva"] = reserva
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{AGENDA_API}/citas/agendar", json=payload)
        return r.json() if r.status_code == 200 else {}

async def confirmar_cita(cita_id: str) -> bool:
    """Cambia estado de Pendiente a Confirmado."""
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{AGENDA_API}/citas/estado", json={
            "cita_id": cita_id,
            "estado": "est-confirmado",
            "por": "pepe"
        })
        return r.status_code == 200

async def cancelar_cita(cita_id: str, motivo: str = "") -> bool:
    """Cancela una cita."""
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{AGENDA_API}/citas/estado", json={
            "cita_id": cita_id,
            "estado": "est-cancelado",
            "por": "pepe",
            "motivo": motivo
        })
        return r.status_code == 200