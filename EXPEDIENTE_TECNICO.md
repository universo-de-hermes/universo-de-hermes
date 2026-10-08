# EXPEDIENTE TÉCNICO — UNIVERSO HERMES

**Versión:** 1.1 — Octubre 2026
**Cliente:** Juan José Otero (jhotas96@gmail.com)
**Repositorio:** https://github.com/universo-de-hermes/universo-de-hermes
**Propósito:** Ecosistema multi-agente para automatización de negocio médico (CJ Medical)

---

## 1. ARQUITECTURA DEL SISTEMA

```
                     INTERNET
                         │
              ┌──────────┴──────────┐
              │     Nginx (:443)     │
              │  (Reverse Proxy SSL) │
              └──────────┬──────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
   ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐
   │  Houdini  │  │   CRM      │  │  Agenda   │
   │  (:∞)     │  │  (:8000)   │  │  (:8001)  │
   │ Telegram  │  │  FastAPI   │  │  FastAPI  │
   │  aiogram  │  │  SQLite    │  │PostgreSQL │
   └─────┬─────┘  └───────────┘  └───────────┘
         │
         │
   ┌─────┴─────────────────────────────┐
   │                                   │
   ├── PostgreSQL 16 (:5432) — pgvector
   │   └── houdini_db (memoria + embeddings)
   │   └── cjmedical (agenda médica)
   │
   ├── SQLite — CRM conversacional
   │
   └── Google APIs (Gmail, Calendar, Sheets, Drive)
```

## 2. INFRAESTRUCTURA (VPS)

| Especificación | Valor |
|----------------|-------|
| **Proveedor** | Hostinger |
| **Plan** | KVM 2 |
| **IP Pública** | 2.25.214.59 |
| **Hostname** | universojota |
| **SO** | Ubuntu 24.04.4 LTS (Noble) |
| **Kernel** | 6.8.0-138-generic |
| **RAM** | 7.8 GB |
| **vCPU** | 2 núcleos |
| **Disco** | 96 GB NVMe |
| **Docker** | Instalado v29.8.0 (sin contenedores activos) |

## 3. COMPONENTES DEL SISTEMA

### 3.1 Houdini (Orquestador)

| Atributo | Detalle |
|----------|---------|
| **Ruta** | `/root/universo/houdini/` |
| **Lenguaje** | Python 3.12.3 |
| **Framework** | aiogram 3.x (Telegram), SQLAlchemy 2.x, asyncpg |
| **Servicio** | `houdini.service` (systemd) |
| **Modelo LLM** | DeepSeek V4 Pro (OpenRouter) |
| **Fallback** | GPT-4o (OpenRouter) |
| **Telegram** | @Houdinipro_bot (ID: 8714100955) |
| **Sub-agentes:** | |
| | Gmail Agent (leer/enviar correos) |
| | Calendar Agent (agenda Google) |
| | Sheets Agent (Google Sheets membresías) |
| | Drive Agent (Google Drive adjuntos) |
| | Telegram Agent (canal principal) |
| | TTS Agent (Salome voz) |
| | WhatsApp Agent (fase 2) |
| | Design Agent (HTML Bootstrap) |
| | Dashboard Agent (membresías VIP) |

### 3.2 Pepe — Recepcionista CJ Medical

| Atributo | Detalle |
|----------|---------|
| **Ruta** | `/root/universo/recepcionista/` |
| **Lenguaje** | Python 3.12.3 |
| **Framework** | python-telegram-bot 22.x, FastAPI, OpenAI |
| **Servicio** | `pepe.service` (systemd) |
| **Modelo** | DeepSeek V4 Pro (OpenRouter) |
| **Telegram** | @CjmedicalBot |
| **CRM** | FastAPI en `crm/server.py` (puerto 8000) |
| **WhatsApp** | Twilio API (pendiente conexión) |
| **Base datos** | SQLite (`crm/cjmedical.db`) |

### 3.3 Agenda CJ Medical

| Atributo | Detalle |
|----------|---------|
| **Ruta** | `/root/universo/agenda/` |
| **Puerto** | 8001 (solo localhost) |
| **Servicio** | `agenda-api.service` (systemd) |
| **Framework** | FastAPI + Uvicorn |
| **Base datos** | PostgreSQL 16 (db: cjmedical, ~10 MB, 15 tablas) |
| **Dominio** | `agenda.universojota.tech` |
| **Admin** | jhotas96@gmail.com |
| **Autenticación** | Login con PBKDF2-SHA256 + cookie de sesión |

### 3.4 Tablero Agendamiento

| Atributo | Detalle |
|----------|---------|
| **Ruta** | `/root/universo/tablero/` |
| **Servicio** | `tablero.service` (systemd) |
| **Función** | Tablero de agendamiento CJ Medical |

## 4. SISTEMA DE DESPLIEGUE

Todos los servicios corren como **systemd units** bajo usuario **root**:

| Servicio | Descripción | Puerto | Tipo |
|----------|-------------|--------|------|
| `houdini.service` | Orquestador Telegram | — | Python |
| `pepe.service` | Recepcionista CRM | — | Python |
| `crm.service` | CRM web panel | 8000 | Python/FastAPI |
| `agenda-api.service` | Agenda CJ Medical | 8001 | Python (localhost) |
| `tablero.service` | Tablero agendamiento | — | Python |
| `nginx.service` | Proxy inverso + SSL | 80/443 | Nginx 1.24 |
| `postgresql.service` | Base de datos | 5432 | PostgreSQL 16 |
| `fail2ban.service` | Anti-brute force | — | Fail2ban |

## 5. DOMINIOS Y SUBDOMINIOS

| URL | Servicio | SSL |
|-----|----------|-----|
| https://agenda.universojota.tech | Agenda CJ Medical | ✅ Let's Encrypt |
| https://crmcjm.universojota.tech | CRM CJ Medical | ✅ Let's Encrypt |

**Eliminados (Oct 2026):** edificio.universojota.tech, houdiniweb.universojota.tech

## 6. SEGURIDAD

| Medida | Estado |
|--------|--------|
| **Firewall** | UFW activo — solo 22, 80, 443 abiertos |
| **SSH** | Solo llave pública, sin contraseña |
| **Root SSH** | `prohibit-password` (solo con llave) |
| **Usuarios** | root, cjm, commanager |
| **Fail2ban** | 3 intentos SSH fallidos → ban (2 IPs baneadas) |
| **HTTPS** | Let's Encrypt — renovación automática |
| **PostgreSQL** | Solo localhost:5432 |
| **unattended-upgrades** | Parches de seguridad automáticos |

## 7. RIESGOS IDENTIFICADOS

### Altos
1. **Puerto 8000 (CRM) expuesto directo** a Internet sin Nginx/SSL
2. **CORS wildcard** en agenda_api.py si ORIGENES=["*"]
3. **Sin rate limiting** en login de agenda
4. **Sin backups automáticos** — PostgreSQL ni SQLite
5. **Sin HSTS, CSP, X-Frame-Options** en Nginx

### Medios
6. **Sin CSRF protection** en agenda
7. **Sin monitoreo ni alertas** si un servicio cae
8. **Token de Google OAuth expirado** (Gmail/Drive no autenticados)
9. **SQLite sin backup ni protección de concurrencia**
10. **IDOR en usuarios** — admin puede modificar/borrar otros admins

## 8. COMANDOS ÚTILES

```bash
# Ver estado de todos los servicios
for s in houdini pepe crm agenda-api tablero nginx postgresql ssh fail2ban; do echo "$s: $(systemctl is-active $s)"; done

# Ver logs de Houdini
journalctl -u houdini -n 50 -f

# Ver logs de Pepe
journalctl -u pepe -n 50 -f

# Ver logs de Agenda API
journalctl -u agenda-api -n 50 -f

# Conectar por SSH desde PC local
ssh -i /c/Users/USER/proyecto\ hermes/vps_key commanager@2.25.214.59

# Subir cambios a GitHub
cd /root/universo && git add . && git commit -m "descripción" && git push

# Fail2ban — ver IPs baneadas
fail2ban-client status sshd
```

## 9. DEPENDENCIAS PRINCIPALES

| Componente | Versión |
|------------|---------|
| Ubuntu | 24.04.4 LTS |
| Python | 3.12.3 |
| Nginx | 1.24.0 |
| PostgreSQL | 16 |
| FastAPI | 0.141.1 |
| Uvicorn | 0.53.0 |
| Fail2ban | Última |
| OpenRouter | deepseek/deepseek-v4-pro |

---

*Documento actualizado Octubre 2026 — Auditoría in-situ del VPS universojota*
