from Book import Book
from Client import Client


class Library:
    def __init__(self):
        self.books = []
        self.clients = []

    def add_book(self, book: Book):
        self.books.append(book)

    def register_client(self, client: Client):
        self.clients.append(client)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def retutn_book(self, book: Book, client: Client):
        book.change_availability(True)
        client.borrowed_books.remove(book)

    def give_book(self, book: Book, client: Client):
        book.change_availability(False)
        client.borrowed_books.append(book)





