class Book:
    def __init__(self, title, author, publication_year, book_id = None, is_borrowed=False, borrowed_by=None):
        # book_id: unique book ID
        # title: book title
        # author: book author
        # publication_year: publication year
        # is_borrowed: kitabın ödünç alınıp alınmadığını tutar
        # borrowed_by: kitabı ödünç alan User objesi veya None
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by

    # User objesini alır
    # Kitabın ödünç alınma durumunu günceller
    # borrowed_by = user
    # is_borrowed = True
    def borrow(self, user):
        self.borrowed_by = user.user_id
        self.is_borrowed = True

    # Kitabı iade durumuna getirir
    # borrowed_by = None
    # is_borrowed = False
    def return_book(self):
        self.borrowed_by = None
        self.is_borrowed = False

    # Book objesini JSON'a uygun dictionary'ye çevirir
    # borrowed_by yerine user_id kaydedilir
    def to_dict(self):
        borrowed_by = self.borrowed_by
        if borrowed_by is not None and hasattr(borrowed_by, "user_id"):
            borrowed_by = borrowed_by.user_id

        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": borrowed_by,
            "type": "book"
        }

    def show_info(self):
        # book_id, title, author, publication_year, is_borrowed ve borrowed_by bilgilerini gösterir
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year} \n")

class Novel(Book):
    def __init__(self, title, author, publication_year, genre, book_id=None, is_borrowed=False, borrowed_by=None):
        # Book'un ortak özelliklerini super().__init__() ile oluştur
        # genre Novel'a özel
        super().__init__(
            title,
            author,
            publication_year,
            book_id=book_id,
            is_borrowed=is_borrowed,
            borrowed_by=borrowed_by,
        )
        self.genre = genre

    def show_info(self):
        # Book'un ortak özelliklerini göster
        # genre'yi de göster
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Genre: {self.genre}\n")

    def to_dict(self):
        borrowed_by = self.borrowed_by
        if borrowed_by is not None and hasattr(borrowed_by, "user_id"):
            borrowed_by = borrowed_by.user_id

        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": borrowed_by,
            "type": "novel",
            "genre": self.genre
        }
    
class Magazine(Book):
    def __init__(self, title, author, publication_year, issue, book_id=None,  is_borrowed=False, borrowed_by=None):
        # Book'un ortak özelliklerini super().__init__() ile oluştur
        # issue Magazine'e özel
        super().__init__(
            title,
            author,
            publication_year,
            book_id=book_id,
            is_borrowed=is_borrowed,
            borrowed_by=borrowed_by,
        )
        self.issue = issue

    def show_info(self):
        # Book'un ortak özelliklerini göster
        # issue'yi de göster
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Issue: {self.issue} \n")
        
    def to_dict(self):
        borrowed_by = self.borrowed_by
        if borrowed_by is not None and hasattr(borrowed_by, "user_id"):
            borrowed_by = borrowed_by.user_id

        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": borrowed_by,
            "type": "magazine",
            "issue": self.issue
        }
