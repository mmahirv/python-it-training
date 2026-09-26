def add_book(books):
    title = input("Title: ")
    author = input("Author: ")

    while True:
        year_input = input("Year: ")
        try:
            year = int(year_input)
            break
        except ValueError:
            print("Lütfen sayı girin!")

    genre = input("Genre: ")

    kitap = {"title": title, "author": author, "year": year, "genre": genre}
    books.append(kitap)


def view_books(books):
    if len(books) == 0:
        print("Kütüphanede hiç kitap yok.")
    else:
        print(f"--- Your Library ({len(books)} book) ---")
        for kitap in books:
            print(kitap["title"], kitap["author"], kitap["year"], kitap["genre"])


def search_books(books):
    terim = input("Arama terimi: ")
    bulundu = False

    for kitap in books:
        if terim.lower() in kitap["title"].lower() or terim.lower() in kitap["author"].lower():
            print(kitap["title"], kitap["author"], kitap["year"], kitap["genre"])
            bulundu = True

    if not bulundu:
        print("Eşleşen kitap bulunamadı.")


def delete_book(books):
    title = input("Silinecek kitabın başlığı: ")

    for kitap in books:
        if kitap["title"].lower() == title.lower():
            books.remove(kitap)
            return True

    return False