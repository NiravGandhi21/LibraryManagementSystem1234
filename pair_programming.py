
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, copies):
        if book_id in self.books:
            raise ValueError("Book ID already exists")

        if copies < 0:
            raise ValueError("Copies cannot be negative")

        self.books[book_id] = {
            "title": title,
            "available_copies": copies
        }

    def check_availability(self, book_id):
        book = self.books.get(book_id)

        if book is None:
            return "Book not found"

        if book["available_copies"] > 0:
            return "Book is available"

        return "Book is not available"


if __name__ == "__main__":
    library = Library()

    library.add_book("B101", "Python Basics", 3)
    library.add_book("B102", "Data Structures", 0)

    print("B101:", library.check_availability("B101"))
    print("B102:", library.check_availability("B102"))
    print("B999:", library.check_availability("B999"))
