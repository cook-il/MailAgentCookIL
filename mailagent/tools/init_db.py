# mailagent/tools/init_db.py

from mailagent.database import db, schema

def initialize_database():
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute(schema.CREATE_KNOWLEDGE_BASE_TABLE)
    cursor.execute(schema.CREATE_LOGS_TABLE)
    cursor.execute(schema.CREATE_MESSAGES_TABLE)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()
