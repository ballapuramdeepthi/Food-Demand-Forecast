from database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

# ==========================================
# FORECAST HISTORY
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS forecast_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_id INTEGER,
    predicted_orders REAL,
    model_used TEXT,
    forecast_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# ==========================================
# INVENTORY
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT,
    current_stock REAL,
    reorder_level REAL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# ==========================================
# AUDIT LOGS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS audit_logs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT,
    details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")