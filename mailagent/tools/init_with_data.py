import sqlite3
from datetime import datetime, timezone

DB_PATH = "mailagent.db"

sample_entries = [
    ("FACT", "Lake Michigan touches Illinois.", "init_script"),
    ("FACT", "The RON project began in 2025.", "init_script"),
    ("RAG", "Cook County is the most populous in Illinois.", "init_script"),
    ("RAG", "Kane County shares services with DuPage.", "init_script"),
    ("FACT", "Web2py was deployed at ai.cook-il.us.", "init_script"),
]

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create table
c.execute("""
CREATE TABLE IF NOT EXISTS knowledge_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    content TEXT,
    source TEXT,
    created_at TEXT,
    approved_by_admin BOOLEAN DEFAULT 0
)
""")

# Insert sample data with timezone-aware UTC timestamps
for entry in sample_entries:
    created_at = datetime.now(timezone.utc).isoformat()
    c.execute("""
        INSERT INTO knowledge_base (type, content, source, created_at, approved_by_admin)
        VALUES (?, ?, ?, ?, 0)
    """, (*entry, created_at))

conn.commit()
conn.close()
print(f"Initialized {DB_PATH} with {len(sample_entries)} test entries.")
