from lib.db.connection import DB_PATH, get_connection
from lib.db.schema import *

def setup_database():
    conn = get_connection()
    with open("lib/db/schema.sql", "r") as file:
        conn.executescript(file.read())
    conn.commit()
    conn.close()
    print(" Alt database setup complete.")

if __name__ == "__main__":
    setup_database()