from lib.models.author import Author
from lib.db.connection import get_connection

def test_create_author_and_fetch_by_name():
    # Clean up any previous test data
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors WHERE full_name = ?", ("Alice Walker",))
    conn.commit()

    # Run test
    author = Author.create("Alice Walker")
    assert isinstance(author.id, int)

    fetched = Author.find_by_name("Alice Walker")
    assert fetched is not None
    assert fetched.id == author.id