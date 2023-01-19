from book import Book

class Library:

    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)


b1 = Book("Harry Potter","J.K. Rowling")
b2 = Book("Fault in my stars","John Green")
l = Library()
print(l.books)

        
