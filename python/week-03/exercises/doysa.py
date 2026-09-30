import csv
from functools import reduce

with open("personeller.csv",'r', encoding="utf-8") as file:
   reader = csv.reader(file)
   
   for row in reader:
       print(f'Ad: {row[0]}, Soyad: {row[1]}, Meslek: {row[2]}, Sehir: {row[3]}, Deneyim: {row[4]}')
       
with open("personeller.csv",'r', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    only_ankara = list(filter(lambda dict: dict['Sehir'] == "Ankara", reader))
    ort_deneyim = reduce(lambda a,b: a + int(b['Deneyim']), only_ankara, 0) / len(only_ankara)                 
    
    print(f'----------------{only_ankara[0]['Sehir']}da Calisanlar-------------')
    
    for insanlar in only_ankara:
       print(f'{insanlar['Ad']} {insanlar['Soyad']} ')
    
    print(f'Toplam ortalama deneyimleri: {ort_deneyim}')