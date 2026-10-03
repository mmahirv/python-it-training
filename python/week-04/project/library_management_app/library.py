import json

from .book import Book, Magazine, Novel
from .user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    # book objesini sisteme ekler
    # book_id üretir:
    # max(existing book_ids) + 1
    # Library boşsa ID = 1
    # book type'a göre Book, Novel veya Magazine objesi oluşturur
    def add_book(self, title, author, publication_year, book_type="book", genre=None, issue=None):

        if len(self.books) == 0:
            book_id = 1
        else:
            max_id = 0

            for book in self.books:
                if book.book_id > max_id:
                    max_id = book.book_id

            book_id = max_id + 1

        if book_type == "novel":
            book = Novel(
                book_id,
                title,
                author,
                publication_year,
                genre
            )

        elif book_type == "magazine":
            book = Magazine(
                book_id,
                title,
                author,
                publication_year,
                issue
            )

        else:
            book = Book(
                book_id,
                title,
                author,
                publication_year
            )

        self.books.append(book)

    # user_id üretir:
    # max(existing user_ids) + 1
    # Library boşsa ID = 1
    #
    # name'in unique olup olmadığını kontrol eder
    # kullanıcı adının boş olup olmadığını kontrol eder
    # password'un geçerli olup olmadığını kontrol eder
    #
    # başarılıysa True
    # başarısızsa False döndürür
    def add_user(self, name, password):

        if name is None or name.strip() == "":
            return False

        for user in self.users:
            if user.name == name:
                return False

        if password is None or password == "":
            return False

        if len(self.users) == 0:
            user_id = 1
        else:
            max_id = 0

            for user in self.users:
                if user.user_id > max_id:
                    max_id = user.user_id

            user_id = max_id + 1

        user = User(user_id, name, password)

        self.users.append(user)

        return True

    # kullanici adi ve sifre kontrolü yapar
    # user objesini döndürür
    # eger user yoksa None döndürür
    def login(self, name, password):

        for user in self.users:
            if user.name == name and user.password == password:
                return user

        return None

    # Library içindeki books ve users verilerini
    # JSON formatına çevirip kaydeder
    def save(self):

        data = {
            "books": [],
            "users": []
        }

        for book in self.books:
            data["books"].append(book.to_dict())

        for user in self.users:
            data["users"].append(user.to_dict())

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    # JSON'dan books ve users verilerini yükler
    # Book / Novel / Magazine objelerini oluşturur
    # User objelerini oluşturur
    # ID'ler üzerinden User ↔ Book ilişkilerini tekrar kurar
    def load(self):

        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return

        self.books = []
        self.users = []

        # Önce user objelerini oluşturuyoruz
        for user_data in data["users"]:

            user = User(
                user_data["user_id"],
                user_data["name"],
                user_data["password"]
            )

            self.users.append(user)

        # Sonra book objelerini oluşturuyoruz
        for book_data in data["books"]:

            if book_data["type"] == "novel":

                book = Novel(
                    book_data["book_id"],
                    book_data["title"],
                    book_data["author"],
                    book_data["publication_year"],
                    book_data["genre"]
                )

            elif book_data["type"] == "magazine":

                book = Magazine(
                    book_data["book_id"],
                    book_data["title"],
                    book_data["author"],
                    book_data["publication_year"],
                    book_data["issue"]
                )

            else:

                book = Book(
                    book_data["book_id"],
                    book_data["title"],
                    book_data["author"],
                    book_data["publication_year"]
                )

            self.books.append(book)

        # User ID'lerini kullanarak User objelerine
        # daha kolay ulaşmak için dictionary oluşturuyoruz
        users_by_id = {}

        for user in self.users:
            users_by_id[user.user_id] = user

        # Book ID'lerini kullanarak Book objelerine
        # daha kolay ulaşmak için dictionary oluşturuyoruz
        books_by_id = {}

        for book in self.books:
            books_by_id[book.book_id] = book

        # Book -> User ilişkisini kuruyoruz
        for book_data in data["books"]:

            book_id = book_data["book_id"]
            borrowed_by = book_data["borrowed_by"]

            if borrowed_by is not None:

                book = books_by_id[book_id]
                user = users_by_id[borrowed_by]

                book.borrowed_by = user
                book.is_borrowed = True

        # User -> Book ilişkisini kuruyoruz
        for user_data in data["users"]:

            user_id = user_data["user_id"]
            user = users_by_id[user_id]

            for book_id in user_data["borrowed_books"]:

                book = books_by_id[book_id]

                user.borrowed_books.append(book)

    # book title alır
    # Library içindeki books listesini arar
    # bulursa aynı Book objesini döndürür
    # bulamazsa None döndürür
    def find_book(self, title):

        for book in self.books:
            if book.title == title:
                return book

        return None

    # Library içindeki bütün kitapları gösterir
    # Her book için show_info() çağırabilir
    def show_all_books(self):

        for book in self.books:
            book.show_info()
            print("--------------------")