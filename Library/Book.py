class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.available = True

    def change_availability(self, available: bool):
        self.available = available

    def book_info(self):
        return f'name: {self.name}, author: {self.author}, year: {self.year}'
