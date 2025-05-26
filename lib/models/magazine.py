from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.id = None

    @classmethod
    def create(cls, name, genre):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, genre) VALUES (?, ?) RETURNING id", (name, genre))
        magazine_id = cursor.fetchone()[0]
        conn.commit()
        magazine = cls(name, genre)
        magazine.id = magazine_id
        return magazine

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            magazine = cls(row[1], row[2])
            magazine.id = row[0]
            return magazine
        return None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            magazine = cls(row[1], row[2])
            magazine.id = row[0]
            return magazine
        return None