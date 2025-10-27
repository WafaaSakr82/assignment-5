class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        print("Books in Library:")
        for book in self.books:
            book.display_info()