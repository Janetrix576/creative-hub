from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")

    writers = [
        ("Nadine Burke",),
        ("Julian Cross",),
        ("Rita Lane",)
    ]
    journals = [
        ("Pen & Pixel", "Creative Writing"),
        ("TechScript", "Technology"),
        ("Mindspace", "Psychology")
    ]
    cursor.executemany("INSERT INTO authors (full_name) VALUES (?)", writers)
    cursor.executemany("INSERT INTO magazines (name, genre) VALUES (?, ?)", journals)

    pieces = [
        ("Shadow & Verse", 1, 1),
        ("Digital Drift", 2, 2),
        ("Mental Landscapes", 3, 3),
        ("Cognition & Code", 2, 3),
        ("Inkwell Echoes", 1, 1),
    ]
    cursor.executemany("INSERT INTO articles (headline, author_id, magazine_id) VALUES (?, ?, ?)", pieces)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_data()