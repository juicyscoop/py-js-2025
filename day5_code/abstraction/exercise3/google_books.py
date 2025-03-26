import urllib.request
# import requests
import json

class GoogleBooks:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        # self.base_url.format(isbn = isbn)
    def get_book(self, isbn):
        response = urllib.request.urlopen(self.base_url.format(isbn=isbn))
        content = json.loads(response.read())
        try:
            book_info = content['items'][0]['volumeInfo']
        except (KeyError, IndexError):
            print('Book with this ISBN not found in Google Books')
            book_info = None
        return book_info
