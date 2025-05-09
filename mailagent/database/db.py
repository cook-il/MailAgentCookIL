import sqlite3

DB_PATH = "mailagent.db"

def get_connection():
    return sqlite3.connect(DB_PATH)


# ========== MESSAGES ==========

def insert_message(sender, command, body):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO messages (sender, command, body, timestamp)
        VALUES (?, ?, ?, ?)
        """,
        (sender, command, body, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

def fetch_all_messages():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM messages ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    conn.close()
    return [dict(zip(columns, row)) for row in rows]


# ========== KNOWLEDGE BASE ==========

def insert_knowledge_entry(contributor, type_, content, source=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO knowledge_base (contributor, type, content, source)
        VALUES (?, ?, ?, ?)
        ''',
        (contributor, type_, content, source)
    )
    conn.commit()
    conn.close()


def fetch_unapproved_entries():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM knowledge_base WHERE approved_by_admin = 0')
    results = cursor.fetchall()
    conn.close()
    return results


def approve_entry(entry_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE knowledge_base SET approved_by_admin = 1 WHERE id = ?',
        (entry_id,)
    )
    conn.commit()
    conn.close()


def delete_entry(entry_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM knowledge_base WHERE id = ?', (entry_id,))
    conn.commit()
    conn.close()
