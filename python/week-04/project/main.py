from library_management_app.user import User
from library_management_app.library import Library
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIBRARY_PATH = os.path.join(BASE_DIR, "data", "library.json")

library = Library('wijchen',[],[])

menu_operations = """===== Library Management System Operations =====
        1 - List all books
        2 - Borrow a book
        3 - Return a book
        4 - Show my borrowed books
        5 - Save and exit
        """
        
menu_login= """
        1 - Login
        2 - Create a new account
        3 - exit
        """
        
library.load_data(LIBRARY_PATH) 
user = None
      
while user is None:
    print(menu_login)
    user_operation = input("Choose an operation: ").strip()
    
    if(user_operation == "1"):
        user_name = input("Enter your name: ").strip().lower()
        user_password = input("Enter your password: ").strip()
        
        user = library.login(user_name, user_password)
        if user:
            print(f"Welcome {user_name.capitalize()}!")
        else:
            print("Invalid username or password. Please try again.")
    
    elif(user_operation == "2"):
        while True:
            user_name = input("Enter your name: ").strip().lower()
            user_password = input("Enter your password: ").strip()

            user = User(user_name, user_password)

            if library.add_user(user):
                print(f"Account created successfully for {user_name.capitalize()}. You can now log in.")
                
                break
            else:
                print("Account creation failed. Username may already exist.")   
    elif(user_operation == "3"):
        print("Exiting the program. Goodbye!")
        break
    
while user is not None:
    print(menu_operations)
    operation = input("Choose an operation: ").strip()
    
    if operation == "1":
        library.list_books()
        
    elif operation == "2":
        book_title = input("Enter the title of the boto borrow: ").strip()
        
        book = library.find_book(book_title)
        
        if book is None: 
            print(f"Book '{book_title}' not found.") 
            continue 
        
        if book.is_borrowed: 
            print( f"Sorry, '{book_title}' is currently " f"borrowed by another user." ) 
            continue 
        
        user.borrow_book(book)
        
        book.borrow(user)
        
        print( f"You have successfully borrowed '{book_title}'." )
        
    elif operation == "3":
        book_title = input("Enter the title of the boto return: ").strip()
        
        book = library.find_book(book_title)
        if book is None: 
            print(f"Book '{book_title}' not found.") 
            continue 
        user.return_book(book)
        
        book.return_book()
        
        print( f"You have successfully returned '{book_title}'." )
        
    elif operation == "4":
        user.list_borrowed_books()
        
    elif operation == "5":
        library.save(LIBRARY_PATH)
        print("Data saved. Exiting...")
        
        break
    
    else:
        print("Invalid operation. Please try again.")