class Book:
def __init__(self, title, author, isbn):
self.title = title
self.author = author
self.isbn = isbn
def __str__(self):
return f"{self.title} by {self.author} (ISBN: {self.isbn})"
class Library:
def __init__(self):
self.books = []
def add_book(self, book: Book):
self.books.append(book)
print(f'Book "{book.title}" added to the library.')
def remove_book(self, isbn: str):
for book in self.books:
if book.isbn == isbn:
self.books.remove(book)
print(f'Book "{book.title}" removed from the library.')
return
print(f"No book found with ISBN {isbn}.")
def display_books(self):
if not self.books:
print("No books available in the library.")
else:
print("\nBooks available in the library:")
for book in self.books:
print(f" - {book}")
if __name__ == "__main__":
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_books()
library.remove_book("9780451524935")
library.display_books()
