import sqlite3

def create_audit_table():

    conn = sqlite3.connect("restaurant.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        details TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def log_action(action, details):

    conn = sqlite3.connect("restaurant.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO audit_logs
    (
        action,
        details
    )
    VALUES (?, ?)
    """, (action, details))

    conn.commit()
    conn.close()