import pytest
from library import Library


def test_add_book():
    library = Library()
    library.add_book("B101", "Python Basics", "John Smith", 3)

    book = library.search_book("B101")

    assert book["title"] == "Python Basics"
    assert book["available_copies"] == 3


def test_search_nonexistent_book():
    library = Library()
    assert library.search_book("B999") is None


def test_duplicate_book():
    library = Library()
    library.add_book("B101", "Python Basics", "John Smith", 3)

    with pytest.raises(ValueError):
        library.add_book(
            "B101", "Advanced Python", "Jane Doe", 2
        )


def test_negative_copies():
    library = Library()

    with pytest.raises(ValueError):
        library.add_book(
            "B102", "Data Structures", "Alex Lee", -1
        )