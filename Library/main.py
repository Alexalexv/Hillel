from Library import Library
from Book import Book
from Client import Client

my_lib = Library()
book1 = Book('Game of Thrones', 'John Snow', '2001')
book2 = Book('Lord of the rings', 'Bilbo Begins', '1950')
book3 = Book('Witcher', 'Geralt of Rivia', '1990')

my_lib.add_book(book1)
my_lib.add_book(book2)
my_lib.add_book(book3)

client1 = Client('Justin Bieber', '+380933007010, New York')
client2 = Client('Macaulay Culkin', '+380933007020, Chicago')

my_lib.register_client(client1)
my_lib.register_client(client2)

my_lib.give_book(book1, client1)

print(book1.available)
print(book2.book_info())