import csv
import json
import os

CSV_FIELDS = ["title", "author", "year", "genre"]

def load_library(filepath):
    """Load books from a JSON file."""
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            books = json.load(file)
    except json.JSONDecodeError:
        print("Kitap dosyasi bozuk veya gecerli JSON biciminde degil.")
        return []
    except OSError:
        print("Kitap dosyasi okunamadi.")
        return []

    if isinstance(books, list):
        return books
    print("Kitap dosyasinda liste bulunamadi.")
    return []


def save_library(filepath, books):
    """Save books to a JSON file."""
    try:
        folder = os.path.dirname(filepath)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
    except OSError:
        print("Kitaplar kaydedilemedi.")


def export_to_csv(books, filepath):
    """Write books to a CSV file."""
    try:
        with open(filepath, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(books)
    except OSError:
        print("CSV dosyasi disa aktarilamadi.")


def import_from_csv(filepath):
    """Read books from a CSV file."""
    try:
        with open(filepath, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames or not all(
                field in reader.fieldnames for field in CSV_FIELDS
            ):
                print("CSV dosyasinda title, author, year ve genre basliklari bulunmali.")
                return []

            books = []
            for row in reader:
                try:
                    book = {
                        "title": row["title"],
                        "author": row["author"],
                        "year": int(row["year"]),
                        "genre": row["genre"],
                    }
                except (KeyError, ValueError, TypeError):
                    print("Gecersiz kitap satiri atlandi.")
                    continue
                books.append(book)
            return books
    except FileNotFoundError:
        print(f"CSV dosyasi bulunamadi: {filepath}")
        return []
    except OSError:
        print("CSV dosyasi okunamadi.")
        return []