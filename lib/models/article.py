from lib.db.connection import get_connection

class Article:
    def __init__(self, headline, author_id, magazine_id):
        self.headline = headline
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.id = None

    @classmethod
    def create(cls, headline, author_id, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO articles (headline, author_id, magazine_id)
            VALUES (?, ?, ?) RETURNING id
        """, (headline, author_id, magazine_id))
        article_id = cursor.fetchone()[0]
        conn.commit()
        article = cls(headline, author_id, magazine_id)
        article.id = article_id
        return article

    @classmethod
    def find_by_headline(cls, headline):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE headline = ?", (headline,))
        row = cursor.fetchone()
        if row:
            article = cls(row[1], row[2], row[3])
            article.id = row[0]
            return article
        return None