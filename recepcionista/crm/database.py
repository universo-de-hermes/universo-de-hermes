"""
CRM CJ Medical - Base de Datos Compartida
Modelos: clientes, mensajes, citas, asesores
"""
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "cjmedical.db")


def get_connection():
    """Obtiene conexión a la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    """Crea las tablas si no existen."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS advisors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            name TEXT NOT NULL,
            role TEXT DEFAULT 'asesor',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id TEXT,
            whatsapp_id TEXT,
            name TEXT,
            phone TEXT,
            email TEXT,
            document TEXT,
            status TEXT DEFAULT 'nuevo',
            channel TEXT DEFAULT 'telegram',
            ai_disabled INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            channel TEXT DEFAULT 'telegram',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        );

        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            city TEXT,
            location TEXT,
            service TEXT,
            professional TEXT,
            date_requested TEXT,
            time_requested TEXT,
            duration TEXT,
            price TEXT,
            zone TEXT,
            package_info TEXT,
            notes TEXT,
            status TEXT DEFAULT 'pendiente',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        );

        CREATE TABLE IF NOT EXISTS pipeline_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            from_status TEXT,
            to_status TEXT,
            changed_by TEXT,
            note TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        );

        CREATE TABLE IF NOT EXISTS pending_replies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            advisor_name TEXT,
            sent INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        );
    """)

    # Crear asesor admin por defecto si no existe
    cursor.execute("SELECT id FROM advisors WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO advisors (username, password_hash, name, role) VALUES (?, ?, ?, ?)",
            ("admin", "admin123", "Administrador", "admin")
        )

    conn.commit()
    conn.close()


# ─── FUNCIONES PARA CLIENTES ───

def get_or_create_client(telegram_id: str, name: str = None) -> dict:
    """Busca o crea un cliente por telegram_id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE telegram_id = ?", (telegram_id,))
    client = cursor.fetchone()
    if client:
        conn.close()
        return dict(client)

    cursor.execute(
        "INSERT INTO clients (telegram_id, name, status, channel) VALUES (?, ?, 'nuevo', 'telegram')",
        (telegram_id, name)
    )
    conn.commit()
    client_id = cursor.lastrowid
    conn.close()
    return {"id": client_id, "telegram_id": telegram_id, "name": name, "status": "nuevo", "channel": "telegram"}


def save_message(client_id: int, role: str, content: str, channel: str = "telegram"):
    """Guarda un mensaje en el historial."""
    conn = get_connection()
    conn.execute(
        "INSERT INTO messages (client_id, role, content, channel) VALUES (?, ?, ?, ?)",
        (client_id, role, content, channel)
    )
    conn.commit()
    conn.close()


def get_conversation(client_id: int) -> list:
    """Obtiene todo el historial de mensajes de un cliente."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM messages WHERE client_id = ? ORDER BY created_at ASC",
        (client_id,)
    )
    messages = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return messages


def update_client_status(client_id: int, status: str, advisor: str = None, note: str = ""):
    """Actualiza el estado del cliente en el pipeline."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM clients WHERE id = ?", (client_id,))
    current = cursor.fetchone()
    if not current:
        conn.close()
        return

    old_status = current["status"]
    cursor.execute("UPDATE clients SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                   (status, client_id))

    # Registrar en pipeline_log
    cursor.execute(
        "INSERT INTO pipeline_log (client_id, from_status, to_status, changed_by, note) VALUES (?, ?, ?, ?, ?)",
        (client_id, old_status, status, advisor, note)
    )
    conn.commit()
    conn.close()


def create_appointment(client_id: int, data: dict) -> int:
    """Crea una solicitud de cita."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO appointments (client_id, city, location, service, professional,
                                  date_requested, time_requested, duration, price,
                                  zone, package_info, notes, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pendiente')
    """, (
        client_id,
        data.get("city"),
        data.get("location"),
        data.get("service"),
        data.get("professional"),
        data.get("date"),
        data.get("time"),
        data.get("duration"),
        data.get("price"),
        data.get("zone"),
        data.get("package"),
        data.get("notes"),
    ))
    conn.commit()
    appointment_id = cursor.lastrowid
    conn.close()
    return appointment_id


def get_all_clients(status: str = None) -> list:
    """Obtiene todos los clientes, opcionalmente filtrados por estado."""
    conn = get_connection()
    cursor = conn.cursor()
    if status:
        cursor.execute("""
            SELECT c.*, COUNT(m.id) as message_count,
                   (SELECT content FROM messages WHERE client_id = c.id ORDER BY created_at DESC LIMIT 1) as last_message
            FROM clients c
            LEFT JOIN messages m ON m.client_id = c.id
            WHERE c.status = ?
            GROUP BY c.id
            ORDER BY c.updated_at DESC
        """, (status,))
    else:
        cursor.execute("""
            SELECT c.*, COUNT(m.id) as message_count,
                   (SELECT content FROM messages WHERE client_id = c.id ORDER BY created_at DESC LIMIT 1) as last_message
            FROM clients c
            LEFT JOIN messages m ON m.client_id = c.id
            GROUP BY c.id
            ORDER BY c.updated_at DESC
        """)
    clients = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return clients


def get_client_detail(client_id: int) -> dict:
    """Obtiene toda la información de un cliente."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
    client = cursor.fetchone()
    if not client:
        conn.close()
        return None
    client = dict(client)

    cursor.execute("SELECT * FROM messages WHERE client_id = ? ORDER BY created_at ASC", (client_id,))
    client["messages"] = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM appointments WHERE client_id = ? ORDER BY created_at DESC", (client_id,))
    client["appointments"] = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM pipeline_log WHERE client_id = ? ORDER BY created_at DESC", (client_id,))
    client["pipeline_log"] = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return client


def update_client_data(client_id: int, **kwargs):
    """Actualiza datos del cliente."""
    if not kwargs:
        return
    fields = ", ".join(f"{k} = ?" for k in kwargs.keys())
    values = list(kwargs.values()) + [client_id]
    conn = get_connection()
    conn.execute(f"UPDATE clients SET {fields}, updated_at = CURRENT_TIMESTAMP WHERE id = ?", values)
    conn.commit()
    conn.close()


def verify_advisor(username: str, password: str) -> dict:
    """Verifica credenciales de asesor."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM advisors WHERE username = ? AND password_hash = ?", (username, password))
    advisor = cursor.fetchone()
    conn.close()
    return dict(advisor) if advisor else None


def get_all_advisors() -> list:
    """Obtiene todos los asesores."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, name, role FROM advisors ORDER BY name")
    advisors = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return advisors