# mailagent/database/schema.py

CREATE_KNOWLEDGE_BASE_TABLE = """
CREATE TABLE IF NOT EXISTS knowledge_base (
    id INTEGER PRIMARY KEY,
    sender TEXT,
    type TEXT,
    content TEXT,
    source TEXT,
    approved_by_admin INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_LOGS_TABLE = """
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY,
    timestamp TEXT,
    sender TEXT,
    command TEXT,
    status TEXT,
    notes TEXT
);
"""

CREATE_MESSAGES_TABLE = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    sender TEXT NOT NULL,
    command TEXT NOT NULL,
    body TEXT,
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
