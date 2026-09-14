class BookNotFoundError(Exception):
    pass
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__price = price
        self.__is_available = True
    def get_price(self):
        return self.__price
    def is_available(self):
        return self.__is_available
    def borrow(self):
        if not self.__is_available:
            return False
        self.__is_available = False
        return True
    def return_book(self):
        self.__is_available = True
    def __str__(self):
        status = "Available" if self.__is_available else "Borrowed"
        return (
            f"{self.book_id} | {self.title} | "
            f"{self.author} | ₹{self.__price} | {status}"
        )
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print("You can borrow maximum 3 books.")
            return
        if book.borrow():
            self.borrowed_books.append(book)
            print("Book borrowed successfully")
        else:
            print("Book is already borrowed")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print("Book returned successfully")
        else:
            print("This book was not borrowed by this member.")

    def display_borrowed_books(self):
        print("\n--------- Borrowed Books ---------")
        if len(self.borrowed_books) == 0:
            print("No books borrowed")
            return
        for book in self.borrowed_books:
            print(book)
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")
    def display_books(self):
        print("\n--------- Library Books ---------")
        if len(self.books) == 0:
            print("No books available")
            return
        for book in self.books:
            print(book)
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook Found:")
                print(book)
                return book
        raise BookNotFoundError("Book Not Found")
    def borrow_book(self, book_id, member):
        for book in self.books:
            if book.book_id == book_id:
                member.borrow_book(book)
                return
        raise BookNotFoundError("Book Not Found")
    def return_book(self, book_id, member):
        for book in self.books:
            if book.book_id == book_id:
                member.return_book(book)
                return
        raise BookNotFoundError("Book Not Found")
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available():
                    print("Cannot remove a borrowed book.")
                    return
                self.books.remove(book)
                print("Book removed successfully")
                return
        raise BookNotFoundError("Book Not Found")
    def available_books(self):
        print("\n--------- Available Books ---------")
        found = False
        for book in self.books:
            if book.is_available():
                print(book)
                found = True
        if not found:
            print("No books available")
library = Library()
book1 = Book(101, "Python Programming", "James", 500)
book2 = Book(102, "SQL Basics", "John", 400)
book3 = Book(103, "Django Beginner", "David", 600)
book4 = Book(104, "Java Programming", "Robert", 550)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.display_books()
member1 = Member(1, "Akshaya")
try:
    library.search_book("Python Programming")
except BookNotFoundError as e:
    print(e)
print("\n--------- Borrowing Books ---------")
try:
    library.borrow_book(101, member1)
    library.borrow_book(102, member1)
except BookNotFoundError as e:
    print(e)
member1.display_borrowed_books()
library.available_books()
print("\n--------- Returning Book ---------")
try:
    library.return_book(101, member1)
except BookNotFoundError as e:
    print(e)
library.available_books()
print("\n--------- Removing Book ---------")
try:
    library.remove_book(104)
except BookNotFoundError as e:
    print(e)
library.display_books()