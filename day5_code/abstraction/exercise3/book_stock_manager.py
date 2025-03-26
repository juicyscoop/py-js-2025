from google_books import GoogleBooks
import json

class BookStockManager:
    def __init__(self):
        self.stock_name = "books.json"
        self.google_books = GoogleBooks()

    def import_into_stock(self, isbn, book_info, price):
        with open('books.json', 'r') as f:
            store_content = json.loads(f.read())
            store_content[isbn] = {
                'title': book_info['title'],
                'authors': ', '.join(book_info['authors']),
                'amount': 0,
                'price': price,
            }
        
        with open('books.json', 'w') as f:
            f.write(json.dumps(store_content))

    def import_book(self, isbn, price):
        book_info = self.google_books.get_book(isbn)
        self.import_into_stock()

