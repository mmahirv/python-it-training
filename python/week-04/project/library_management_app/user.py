class User:
    # name: str
    # password: str
    # borrowed_books: list[Book]
    # Runtime'da kullanıcının ödünç aldığı Book objelerini tutar.
    # JSON'a kaydedilirken Book objeleri yerine book_id'leri tutulur.

    def __init__():
        pass

    # Book objesi alır.
    # Kullanıcının borrowed_books listesine ekler.
    # Kitabın borrow işlemini gerçekleştirir Book.
    def borrow_book():
        pass

    # Book objesi alır.
    # Kitabın return işlemini gerçekleştirir.
    # Kitabı borrowed_books listesinden çıkarır.
    def return_book():
        pass

    # Kullanıcının ödünç aldığı kitapları listeler.
    def list_borrowed_books():
        pass

    # User objesini JSON'a uygun dictionary formatına çevirir.
    # borrowed_books içindeki Book objeleri yerine book_id'leri kaydeder.
    def to_dict():
        pass
