class library():
    avialableBooks=[]
    landedBook={}
    
    def __init__(self,avialableBooks,library_name) :
        self.avialableBooks=avialableBooks
        self.library_name=library_name

    def display_book(self):
        return self.avialableBooks
    
    def lend_book(self,name,book):
        self.avialableBooks.remove(book)
        self.landedBook[book]=name
        return 
    
    def add_book(self,book):
        self.avialableBooks.append(book)
        return
        
    
    def return_book(self,book):
        self.avialableBooks.append(book)
        self.landedBook.pop(book)
        return
    
