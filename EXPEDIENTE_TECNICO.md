# EXPEDIENTE TÉCNICO — UNIVERSO HERMES

**Versión:** 1.0 — Septiembre 2026
**Cliente:** Juan José Otero (jhotas96@gmail.com)
**Repositorio:** https://github.com/universo-de-hermes/universo-de-hermes
**Propósito:** Ecosistema multi-agente para automatización de negocio médico (CJ Medical) y gestión de redes sociales

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
   │  Houdini  │  │   Web UI  │  │   CRM      │
   │  (:∞)     │  │  (:9999)  │  │  (:8000)   │
   │ Telegram  │  │  Node.js  │  │  FastAPI   │
   │  aiogram  │  │  Express  │  │  SQLite    │
   └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
         │              │              │
         │      ┌───────┴───────┐      │
         │      │ HoudiniBridge │      │
         │      │   (:9876)     │      │
         │      │  Python HTTP  │      │
         │      └───────────────┘      │
         │                             │
   ┌─────┴─────────────────────────────┘
   │
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
| **Disco** | 96 GB NVMe (15% usado) |
| **Swap** | Sin configurar |
| **Uptime** | 13 días |
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
| **Modelo** | Claude Haiku (Anthropic) |
| **Telegram** | @CjmedicalBot |
| **CRM** | FastAPI en `crm/server.py` (puerto 8000) |
| **WhatsApp** | Twilio API (pendiente conexión) |
| **Base datos** | SQLite (`crm/cjmedical.db`) |

### 3.3 Command Center 3D
| Atributo | Detalle |
|----------|---------|
| **Ruta** | `/root/universo/server_api.py` |
| **Plantilla** | `Command Center Oficina.html` (83KB) |
| **Puerto** | 3000 |
| **Servicio** | `command-center.service` (systemd) |
| **Tecnología** | Python http.server + Three.js + React (CDN) |
| **Función** | Visualización 3D de agentes en tiempo real |
| **API** | `/api/status`, `/api/flow`, `/api/assign`, `/api/complete`, `/api/fire` |

### 3.4 Web UI — Orbe Houdini
| Atributo | Detalle |
|----------|---------|
| **Ruta** | `/root/universo/web-ui/` |
| **Frontend** | Vite + Three.js + Express backend |
| **Backend** | Node.js 20.20.2 (puerto 9999) |
| **Bridge** | Python (puerto 9876, solo localhost) |
| **Servicio** | `webui-backend.service` + `houdini-bridge.service` |
| **Función** | Interfaz 3D tipo orbe para interactuar con Houdini |

### 3.5 Social Responder — Community Manager
| Atributo | Detalle |
|----------|---------|
| **Ruta** | `/root/universo/social-responder/` |
| **Puerto** | 3005 |
| **Endpoint** | `POST /webhook/meta/` |
| **Meta App** | Hermes Community Manager (ID: 1562958188389751) |
| **Función** | Responder comentarios en IG/FB |
| **Estado** | Webhook activo, IG @cejas_catalinajaramillo pendiente |

### 3.6 Agenda API
| Atributo | Detalle |
|----------|---------|
| **Ruta** | `/root/universo/agenda/` |
| **Puerto** | 8001 (solo localhost) |
| **Autenticación** | Token por header `X-API-Token` |
| **Dominio** | `agenda.universojota.tech` |
| **Base datos** | PostgreSQL (db: cjmedical) |
| **Admin** | jhotas96@gmail.com |

## 4. SISTEMA DE DESPLIEGUE

Todos los servicios corren como **systemd units** bajo usuario **root**:

| Servicio | Descripción | Puerto | Tipo |
|----------|-------------|--------|------|
| `houdini.service` | Orquestador Telegram | — | Python |
| `pepe.service` | Recepcionista CRM | — | Python |
| `crm.service` | CRM web panel | 8000 | Python/FastAPI |
| `command-center.service` | Edificio 3D | 3000 | Python |
| `social-responder.service` | Webhook redes | 3005 | Python |
| `agenda-api.service` | Agenda CJ Medical | 8001 | Python (localhost) |
| `webui-backend.service` | Orbe backend | 9999 | Node.js |
| `houdini-bridge.service` | Bridge orbe→Houdini | 9876 | Python (localhost) |
| `nginx.service` | Proxy inverso + SSL | 80/443 | Nginx 1.24 |
| `postgresql.service` | Base de datos | 5432 | PostgreSQL 16 |
| `fail2ban.service` | Anti-brute force | — | Fail2ban |

## 5. DOMINIOS Y SUBDOMINIOS

| URL | Servicio | SSL |
|-----|----------|-----|
| https://edificio.universojota.tech | Command Center 3D | ✅ Let's Encrypt |
| https://houdiniweb.universojota.tech | Web UI Orbe | ✅ Let's Encrypt |
| https://crmcjm.universojota.tech | CRM CJ Medical | ✅ Let's Encrypt |
| https://agenda.universojota.tech | Agenda API (en preparación) | Pendiente |

## 6. SEGURIDAD

| Medida | Estado |
|--------|--------|
| **Firewall** | UFW activo — solo 22, 80, 443 abiertos |
| **SSH** | Solo llave pública, sin contraseña |
| **Root SSH** | `prohibit-password` (solo con llave) |
| **Usuarios** | root, commanager, cjm, edificio (cada uno con su rol) |
| **Fail2ban** | 3 intentos SSH fallidos → ban 24h (2 IPs baneadas) |
| **HTTPS** | Let's Encrypt — renovación automática |
| **PostgreSQL** | Solo localhost:5432 |
| **API Agenda** | Protegida con token X-API-Token |
| **Monitoreo** | Cada 5 minutos → alerta Telegram si servicio cae |
| **Backups** | Diarios 3 AM — PostgreSQL + SQLite + archivos (retención 7 días) |
| **unattended-upgrades** | Parches de seguridad automáticos |
| **Secretos en código** | ❌ Riesgo: verify_token hardcodeado en webhook |

## 7. BACKUPS

```
/backup/
├── postgres/
│   ├── houdini_YYYYMMDD_HHMM.dump  (PostgreSQL — 17KB)
│   └── cjmedical_YYYYMMDD_HHMM.db  (SQLite CRM)
└── files/
    └── universo_YYYYMMDD_HHMM.tar.gz  (código fuente — 55KB)
```

| Detalle | Valor |
|---------|-------|
| **Frecuencia** | Diaria 3:00 AM |
| **Retención** | 7 días |
| **Cron** | `/etc/cron.d/universo` |
| **Script** | `/usr/local/bin/universo-backup.sh` |
| **Monitoreo** | Al servicio y backup en log `/var/log/universo-backup.log` |

## 8. RIESGOS IDENTIFICADOS

### Críticos
1. **API Command Center sin autenticación** — cualquiera puede ejecutar POST en `/api/fire`
2. **Sin control de versiones remoto** — resuelto con GitHub hoy
3. **Backups en mismo VPS** — pérdida total si el servidor falla
4. **Variables .env no respaldadas**
5. **Puertos 3000/3005/8000/9999 accesibles desde internet** (UFW bypass)

### Altos
6. **CORS con `Access-Control-Allow-Origin: *`** en todas las APIs
7. **Sin rate limiting** — posible abuso/DoS
8. **PostgreSQL en modo trust para localhost**
9. **Secretos hardcodeados** en webhook_server.py

### Medios
10. Todos los servicios como root
11. Sin validación de entrada en APIs
12. Sin tokens CSRF
13. Reboot del sistema pendiente

## 9. COMANDOS ÚTILES

```bash
# Ver estado de todos los servicios
for s in houdini pepe crm command-center webui-backend houdini-bridge nginx postgresql ssh fail2ban; do echo "$s: $(systemctl is-active $s)"; done

# Ver logs de Houdini
journalctl -u houdini -n 50 -f

# Ver logs de Pepe
journalctl -u pepe -n 50 -f

# Backup manual
/usr/local/bin/universo-backup.sh

# Conectar por SSH desde PC local
ssh -i /c/Users/USER/proyecto\ hermes/vps_key commanager@2.25.214.59

# Subir cambios a GitHub
cd /root/universo && git add . && git commit -m "descripción" && git push

# Fail2ban — ver IPs baneadas
fail2ban-client status sshd
```

## 10. DEPENDENCIAS PRINCIPALES

| Componente | Versión |
|------------|---------|
| Ubuntu | 24.04.4 LTS |
| Python | 3.12.3 |
| Node.js | 20.20.2 |
| Nginx | 1.24.0 |
| PostgreSQL | 16.15 |
| Docker | 29.8.0 |
| Fail2ban | Última |
| OpenRouter | deepseek/deepseek-v4-pro |
| Anthropic | claude-haiku-4-5-20251001 |

---

*Documento generado el 22 Septiembre 2026 — Auditoría in-situ del VPS universojota*