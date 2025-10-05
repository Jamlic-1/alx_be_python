# === library_management.py ===
class Book:
def __init__(self, title: str, author: str):
self.title = title
self.author = author
self._is_checked_out = False


def check_out(self) -> bool:
if self._is_checked_out:
return False
self._is_checked_out = True
return True


def return_book(self) -> bool:
if not self._is_checked_out:
return False
self._is_checked_out = False
return True


def is_available(self) -> bool:
return not self._is_checked_out




class Library:
def __init__(self):
self._books = []


def add_book(self, book: Book) -> None:
self._books.append(book)


def check_out_book(self, title: str) -> None:
for book in self._books:
if book.title == title and book.is_available():
book.check_out()
return


def return_book(self, title: str) -> None:
for book in self._books:
if book.title == title and not book.is_available():
book.return_book()
return


def list_available_books(self) -> None:
for book in self._books:
if book.is_available():
print(f"{book.title} by {book.author}")




# === library_main.py (example runner for the library) ===
from library_management import Book, Library




def main():
library = Library()
library.add_book(Book("Brave New World", "Aldous Huxley"))
library.add_book(Book("1984", "George Orwell"))


print("Available books after setup:")
library.list_available_books()


library.check_out_book("1984")
print("\nAvailable books after checking out '1984':")
library.list_available_books()


library.return_book("1984")
print("\nAvailable books after returning '1984':")
library.list_available_books()




if __name__ == "__main__":
main()
