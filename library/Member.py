class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id  # private attribute
        self.borrowed_books = []
    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrowed '{book.title}'")
    # Getter and Setter for membership_id
    def get_membership_id(self):
        return self.__membership_id

    def set_membership_id(self, new_id):
        self.__membership_id = new_id