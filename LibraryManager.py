class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self, ISBN, title, author, publisher, year, volume=None, topic=None):
        book = {
            "ISBN": ISBN,
            "title": title,
            "author": author,
            "publisher": publisher,
            "year": year,
            "volume": volume,
            "topic": topic
        }
        self.books.append(book)

    def remove_book(self, ISBN):
        self.books = [book for book in self.books if book["ISBN"] != ISBN]

    def book_details(self, ISBN):
        for book in self.books:
            if book["ISBN"] == ISBN:
                return book
        return None

    def search_books(self, query):
        results = []
        for book in self.books:
            if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
                results.append(book)
        return results

    def list_books(self):
        return self.books

    def update_details(self, ISBN, **kwargs):
        for book in self.books:
            if book["ISBN"] == ISBN:
                for key, value in kwargs.items():
                    if key in book:
                        book[key] = value
                return True
        return False

    def is_book_available(self, ISBN):
        for book in self.books:
            if book["ISBN"] == ISBN:
                return True
        return False

