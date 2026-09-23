urunler = ["Telefon", "Bilgisayar", "Kulaklık", "Tablet"]
stok_durumu = [True, False, True, False] # Telefon ve Kulaklık stokta var

# zip(urunler, stok_durumu) -> [('Telefon', True), ('Bilgisayar', False), ...] üretir.
# lambda fonksiyonu bu ikilileri (tuple) alır ve ikincisi (stok) True olanları seçer.
filtreli_obje = filter(lambda eleman: eleman[1] == True, zip(urunler, stok_durumu))

# Sadece ürün isimlerini almak için listeye çevirip ekrana basalım
# eleman[0] bize ürünün adını verir
sonuc = [urun[0] for urun in filtreli_obje]

print(sonuc)
# Çıktı: ['Telefon', 'Kulaklık']


tum_ogrenciler = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Can"]
sinavi_gecenler = ["Ayşe", "Can", "Ahmet"]

# tum_ogrenciler listesindeki her bir elemanı kontrol et: 
# Eğer eleman sinavi_gecenler listesinin İÇİNDEYSE (in) tut.
gecen_ogrenciler = filter(lambda ogrenci: ogrenci in sinavi_gecenler, tum_ogrenciler)

print(list(gecen_ogrenciler))
# Çıktı: ['Ahmet', 'Ayşe', 'Can']

diveders = range(2,11)

asal_sayilar = filter((lambda x: all((x % i != 0 or x == i) for i in diveders)),range(2,101))
print(list(asal_sayilar))