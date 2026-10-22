
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, copies):
        if not isinstance(book_id, str) or not book_id.strip():
            raise ValueError("Book ID cannot be empty")

        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title cannot be empty")

        if not isinstance(author, str) or not author.strip():
            raise ValueError("Author cannot be empty")

        if isinstance(copies, bool) or not isinstance(copies, int):
            raise ValueError("Copies must be an integer")

        if book_id in self.books:
            raise ValueError("Book ID already exists")

        if copies < 0:
            raise ValueError("Copies cannot be negative")

        self.books[book_id] = {
            "book_id": book_id,
            "title": title,
            "author": author,
            "total_copies": copies,
            "available_copies": copies,
        }

    def search_book(self, book_id):
        return self.books.get(book_id)
