# mailagent/tools/init_db.py
import sqlite3

conn = sqlite3.connect("mailagent.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS knowledge_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    content TEXT,
    source TEXT,
    created_at TEXT,
    approved_by_admin BOOLEAN
)
""")
conn.commit()
conn.close()
print("mailagent.db initialized.")
