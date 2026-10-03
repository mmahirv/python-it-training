class User:


    def __init__(self, name, password, user_id=None):
        
        self.user_id = user_id
        self.name = name
        self.password = password
        self.borrowed_books = []

    
    def borrow_book(self, book):
        if book.borrow(self):
            self.borrowed_books.append(book)
            return True
        return False

    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False


    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("You have no borrowed books.")
            return
        for book in self.borrowed_books:
            book.show_info()


    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "password": self.password,
            "borrowed_books": [book.book_id for book in self.borrowed_books],
        }