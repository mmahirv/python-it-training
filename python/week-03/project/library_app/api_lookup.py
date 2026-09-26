# By https://github.com/nksecurity
# Retrieves the author and year information for the book via the Open Library API.
# return type {"author": author, "year": year} 
try:
    import requests
except ImportError:
    requests = None

def lookup_book(title):   
    if requests is None:
        print("'requests' kurulu değil. Kurmak için: pip3 install requests")
        return None
    
#Baslik yazilmadi ise ekrana uyari yaz
    if not title or not title.strip():
        print("Baslik bos olamaz!")
        return None
    title=title.strip()

#Apiye istek gonder olasi hata mesajlarini yaz
    try:
        response=requests.get(
            "https://openlibrary.org/search.json",
            params={"title": title, "limit":10},
            timeout=5,
        )
        response.raise_for_status()
        data=response.json()
    except requests.exceptions.Timeout:
        print("Istek zaman asimina ugradi.")
        return None 
    except requests.exceptions.ConnectionError:
        print("Internet Baglantisi Yok.")
        return None
    except ValueError:
        print("Sunucudan gelen dosya okunamadi.")
        return None
    except requests.exceptions.HTTPError:
        print("Sunucu hata verdi, daha sonra tekrar deneyin.")
        return None
    except requests.exceptions.RequestException:
        print("Istek sirasinda beklenmeyen bir hata oldu.")
        return None
#Apiden gelen bilgileri al
    if not isinstance (data,dict):
        print("Sunucudan beklenmeyen bir sorun oldu.")
        return None
    
    docs=data.get("docs")
    if not docs:
        print("Kitap bulunamadi.")
        return None
#Yazari ve yilina gore kitabi bul
    for book in docs:
        authors = book.get("author_name")
        year = book.get("first_publish_year")
        if authors and isinstance(year, int):
            return {"author": authors[0], "year":year}
#Sorgu bitti ve uygun kitap cikmadi mesaj
    print("Kitap var ama yazar ve yil bilgileri eksik.")
    return None