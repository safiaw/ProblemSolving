from book import Book

class Library:

    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)


class LibraryBook(Book):

    def __init__(self, title, author, inventory):
        super().__init__(title, author)
        self.inventory = inventory
        self.borrowers = []

    def check_out(self,name):

        if self.inventory < 1:
            print("Sorry, not available")
            return
        self.inventory -=1
        self.borrowers.append(name)
        
    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Inventory remaining: {self.inventory}")
        print(f"Borrowers: {', '.join(self.borrowers)}")
        
        
        

#b1 = Book("Harry Potter","J.K. Rowling")
#b2 = Book("Fault in my stars","John Green")
#l = Library()
#l.add_book(b1)
#l.add_book(b2)
#print(l.books)
b = LibraryBook("Harry Potter","J.K. Rowling",2)
b.check_out("Safia")
b.print_info()
b.check_out("Rashid")
b.print_info()
