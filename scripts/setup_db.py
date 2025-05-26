import sqlite3
from lib.db.connection import DB_PATH

def setup_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open("lib/db/schema.sql", "r") as f:
        schema = f.read()
        cursor.executescript(schema)

    conn.commit()
    conn.close()
    print("✅ Database setup complete.")

if __name__ == "__main__":
    setup_database()