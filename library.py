class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, copies):
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