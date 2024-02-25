from library import library
import os
import pickle

# Check if the file exists
if os.path.exists('books.pkl'):
    # If the file exists, load the list from the file
    with open('books.pkl', 'rb') as f:
        myAvailableBook = pickle.load(f)
else:
    # If the file does not exist, initialize an empty list
    myAvailableBook = []
    
mylibrary=library(myAvailableBook,"London Library")

if __name__ == "__main__":

    def showBook():
        myAvailableBook=mylibrary.display_book()
        if(len(myAvailableBook)>=1):
                print("Available books are ")
                for book in myAvailableBook:
                    print(book)
        else:
                print("\nThere is no book available.")
    
    while(True):
        print()
        print("Welcome to London Library".center(50, '-'))
        userInput=int(input('''                         
                        What you want to do?
                            
                        press 1 for see available book, 
                        2 for to add book, 
                        3 for to lend book, 
                        4 for to return book 
                        5 to exit    
                        '''))

        if(userInput==1):
            showBook()
        elif(userInput==2):
            book=input("\nEnter the name of book to add: ")
            mylibrary.add_book(book)
            
            print("\nBook has been added to library.")
            
        elif(userInput==3):
            userName=input("Enter the name of user: ")
            print(mylibrary.display_book())
            bookName=input("\nEnter the name of book from above list: ")
            mylibrary.lend_book(userName,bookName)
            print(f"{bookName} has lended to {userName}")
        elif(userInput==4):
            print(mylibrary.landedBook.keys())
            book=input("\nEnter the name of book to retun from above list: ")
            mylibrary.return_book(book)
            print(f"{book} has returned to library. Now avaibale books are ")
            showBook()
        elif(userInput==5):
            break
        else:
            print("Wrong input")

    with open('books.pkl', 'wb') as f:
        pickle.dump(myAvailableBook, f)