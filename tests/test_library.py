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


def test_zero_copies_allowed():
    library = Library()
    library.add_book("B103", "Python Basics", "John Smith", 0)

    book = library.search_book("B103")
    assert book["available_copies"] == 0


def test_empty_title_rejected():
    library = Library()

    with pytest.raises(ValueError):
        library.add_book("B104", "", "John Smith", 2)

    assert library.search_book("B104") is None


def test_non_integer_copies_rejected():
    library = Library()

    with pytest.raises(ValueError):
        library.add_book("B105", "Python Basics", "John Smith", 2.5)

    assert library.search_book("B105") is None
