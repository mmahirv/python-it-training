import os
from library_app.api_lookup import lookup_book
from library_app.book_operations import (
    add_book,
    delete_book,
    search_books,
    view_books,
)
from library_app.file_handler import (
    export_to_csv,
    import_from_csv,
    load_library,
    save_library,
)

DATA_PATH = os.path.join("data", "library.json")


def main_menu():
    print("\n===== Personal Library Manager =====")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search books")
    print("4. Delete a book")
    print("5. Export to CSV")
    print("6. Import from CSV")
    print("7. Add book via Online Lookup (Bonus)")
    print("8. Exit")
    return input("Choose an option: ").strip()


def main():
    books = load_library(DATA_PATH)

    while True:
        choice = main_menu()

        if choice == "1":
            add_book(books)
            save_library(DATA_PATH, books)

        elif choice == "2":
            view_books(books)

        elif choice == "3":
            search_books(books)

        elif choice == "4":
            if delete_book(books):
                save_library(DATA_PATH, books)

        elif choice == "5":
            csv_path = input(
                "Dışa aktarılacak CSV dosya adı/yolu (Örn: export.csv): "
            ).strip()
            if csv_path:
                export_to_csv(books, csv_path)

        elif choice == "6":
            csv_path = input(
                "İçe aktarılacak CSV dosya adı/yolu (Örn: export.csv): "
            ).strip()
            imported = import_from_csv(csv_path)
            if imported:
                books.extend(imported)
                save_library(DATA_PATH, books)

        elif choice == "7":
            title = input("Aranacak Kitap Başlığı (Title): ").strip()
            api_result = lookup_book(title)

            if api_result:
                print(
                    f"\n[API Buldu] Yazar: {api_result['author']} | Yıl: {api_result['year']}"
                )
                genre = input("Genre (Tür): ").strip()

                try:
                    year_val = int(api_result["year"])
                except ValueError:
                    year_val = 0

                new_book = {
                    "title": title,
                    "author": api_result["author"],
                    "year": year_val,
                    "genre": genre,
                }
                books.append(new_book)
                save_library(DATA_PATH, books)
                print("Kitap başarıyla eklendi ve kaydedildi!")
            else:
                print("Lütfen bilgileri manuel ekleyin:")
                add_book(books)
                save_library(DATA_PATH, books)

        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Geçersiz seçenek! Lütfen 1-8 arasında bir seçim yapın.")


if __name__ == "__main__":
    main()