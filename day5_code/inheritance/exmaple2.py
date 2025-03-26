

class Book:
    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author

    def print_book_info(self):
        print(f"Book name: {self.name} ||| Book price: {self.price} ||| Book author: {self.author}")

class EBook(Book):
    def print_book_info(self, additional_info):
        super().print_book_info()
        print(f"ELECTRONIC BOOK -> book name: {self.name} --- {additional_info}")

b = Book(
    name="harry potter",
    price=10,
    author="J. K. Rowling"
)
b.print_book_info()

e = EBook(
    name="Lord of the rings",
    price=8,
    author="J. R. R. Tolkien"
)
e.print_book_info()
