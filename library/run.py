from Book import Book
from Library import Library
from Member import Member
from StaffMember import StaffMember

# Create library
library = Library()

# Create staff member/add books
staff = StaffMember("Ali", "M109", "A001")
book1 = Book("Programming", "Gosef", "123490")
book2 = Book("Python Language", "Andrew", "098321")
staff.add_book(library, book1)
staff.add_book(library, book2)

# Create a member, borrow/try to borrow/return books
member = Member("Hani", "M109")
member.borrow_book(book1)
member.borrow_book(book1)
member.return_book(book1)

# Display books again
library.display_books()




