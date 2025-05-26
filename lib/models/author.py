from lib.db.connection import get_connection

class Author:
    def __init__(self, full_name):
        self.full_name = full_name
        self.id = None

    @classmethod
    def create(cls, full_name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (full_name) VALUES (?) RETURNING id", (full_name,))
        author_id = cursor.fetchone()[0]
        conn.commit()
        author = cls(full_name)
        author.id = author_id
        return author

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            author = cls(row[1])
            author.id = row[0]
            return author
        return None

    @classmethod
    def find_by_name(cls, full_name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE full_name = ?", (full_name,))
        row = cursor.fetchone()
        if row:
            author = cls(row[1])
            author.id = row[0]
            return author
        return None