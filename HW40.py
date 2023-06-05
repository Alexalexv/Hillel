class BookCatalog:
    def search_book(self, title):
        print(f"Searching for book: {title}")

    def checkout_book(self, title):
        print(f"Checking out book: {title}")

    def return_book(self, title):
        print(f"Returning book: {title}")


class MagazineCatalog:
    def search_magazine(self, title):
        print(f"Searching for magazine: {title}")

    def checkout_magazine(self, title):
        print(f"Checking out magazine: {title}")

    def return_magazine(self, title):
        print(f"Returning magazine: {title}")


class LibraryFacade:
    def __init__(self):
        self.book_catalog = BookCatalog()
        self.magazine_catalog = MagazineCatalog()

    def search_book(self, title):
        self.book_catalog.search_book(title)

    def checkout_book(self, title):
        self.book_catalog.checkout_book(title)

    def return_book(self, title):
        self.book_catalog.return_book(title)

    def search_magazine(self, title):
        self.magazine_catalog.search_magazine(title)

    def checkout_magazine(self, title):
        self.magazine_catalog.checkout_magazine(title)

    def return_magazine(self, title):
        self.magazine_catalog.return_magazine(title)


library = LibraryFacade()
library.search_book("Буквар")
library.checkout_book("Буквар")
library.return_book("Буквар")
library.search_magazine("Ромашка")
library.checkout_magazine("Ромашка")
library.return_magazine("Ромашка")
