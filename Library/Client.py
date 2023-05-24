from Person import Person
from Book import Book


class Client(Person):
    def __init__(self, name, contact):
        super().__init__(name, contact)
        self.rating = 0
        self.borrowed_books = []

    def return_book(self, book: Book):
        book.available = True
        self.borrowed_books.remove(book)

    @property
    def client_info(self):
        return f'name: {self.name}, contact: {self.contact}'
