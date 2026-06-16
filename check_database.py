import sqlite3

conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [table[0] for table in cursor.fetchall()]

print("===== TABLES IN DATABASE =====")
print(tables)

# Check forecast_history
if "forecast_history" in tables:
    print("\n===== FORECAST HISTORY =====")
    cursor.execute("SELECT * FROM forecast_history")
    for row in cursor.fetchall():
        print(row)
else:
    print("\nforecast_history table not found")

# Check inventory
if "inventory" in tables:
    print("\n===== INVENTORY =====")
    cursor.execute("SELECT * FROM inventory")
    for row in cursor.fetchall():
        print(row)
else:
    print("\ninventory table not found")

# Check audit_logs
if "audit_logs" in tables:
    print("\n===== AUDIT LOGS =====")
    cursor.execute("SELECT * FROM audit_logs")
    for row in cursor.fetchall():
        print(row)
else:
    print("\naudit_logs table not found")

conn.close()