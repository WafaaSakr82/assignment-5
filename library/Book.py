class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn  # private attribute
        self.available = True

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}, Available: {self.available}")

    # Getter and Setter for ISBN
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn









