class Book:
    def __init__():
        # book_id: unique book ID
        # title: book title
        # author: book author
        # publication_year: publication year
        # is_borrowed: kitabın ödünç alınıp alınmadığını tutar
        # borrowed_by: kitabı ödünç alan User objesi veya None
        pass

    # User objesini alır
    # Kitabın ödünç alınma durumunu günceller
    # borrowed_by = user
    # is_borrowed = True
    def borrow():
        pass

    # Kitabı iade durumuna getirir
    # borrowed_by = None
    # is_borrowed = False
    def return_book():
        pass

    # Book objesini JSON'a uygun dictionary'ye çevirir
    # borrowed_by yerine user_id kaydedilir
    def to_dict():
        pass
    
    def show_info():
        # book_id, title, author, publication_year, is_borrowed ve borrowed_by bilgilerini gösterir
        pass

class Novel(Book):
    def __init__():
        # Book'un ortak özelliklerini super().__init__() ile oluştur
        # genre Novel'a özel
        pass

    def show_info():
        # Book'un ortak özelliklerini göster
        # genre'yi de göster
        pass
    
class Magazine(Book):
    def __init__():
        # Book'un ortak özelliklerini super().__init__() ile oluştur
        # issue Magazine'e özel
        pass
    
    def show_info():
        # Book'un ortak özelliklerini göster
        # issue'yi de göster
        pass