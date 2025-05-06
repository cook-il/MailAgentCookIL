import sqlite3

def initialize_db(path="mailagent.db"):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    # Table for storing raw emails
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT NOT NULL,
        command TEXT NOT NULL,
        body TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Table for RAG and fact inputs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS knowledge_base (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contributor TEXT NOT NULL,
        type TEXT CHECK(type IN ('fact', 'rag')) NOT NULL,
        content TEXT NOT NULL,
        source TEXT,
        approved_by_admin INTEGER DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()
