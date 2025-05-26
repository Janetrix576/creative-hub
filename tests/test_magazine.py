from lib.models.magazine import Magazine

def test_create_magazine_and_find_by_name():
    magazine = Magazine.create("Nature Weekly", "Science")
    assert isinstance(magazine.id, int)

    fetched = Magazine.find_by_name("Nature Weekly")
    assert fetched is not None
    assert fetched.genre == "Science"