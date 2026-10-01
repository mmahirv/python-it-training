from .book import Book, Magazine, Novel
from .user import User

class Library:
    def __init__():
        pass

    # book objesini sisteme ekler
    # book_id üretir:
    # max(existing book_ids) + 1
    # Library boşsa ID = 1
    # book type'a göre Book, Novel veya Magazine objesi oluşturur
    def add_book():
        pass

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
    def add_user():
        pass
    
    #kullanici adi ve sifre kontrolü yapar
    #use objesini döndürür
    #eger user yoksa None döndürür
    def login():
        pass

    # Library içindeki books ve users verilerini
    # JSON formatına çevirip kaydeder
    def save(self):
        pass

    # JSON'dan books ve users verilerini yükler
    # Book / Novel / Magazine objelerini oluşturur
    # User objelerini oluşturur
    # ID'ler üzerinden User ↔ Book ilişkilerini tekrar kurar
    def load(self):
        pass

    # book title alır
    # Library içindeki books listesini arar
    # bulursa aynı Book objesini döndürür
    # bulamazsa None döndürür
    def find_book(self):
        pass

    # Library içindeki bütün kitapları gösterir
    # Her book için show_info() çağırabilir
    def show_all_books(self):
        pass