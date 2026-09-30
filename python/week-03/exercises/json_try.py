import os
import json

klasor = 'Raporlar'
if not os.path.exists(klasor):
    os.mkdir(klasor)
    print(f'{klasor} klasorunuz hazir!')
    
info = '{"ad":"Ayse", "yas":22, "diller":["Python","C#"]}'

infoDict = json.loads(info)

print(infoDict)

info2 = {"ad":"Ayse", "soyad": "Kozan", "Bolum":'yazilim', "dersler":["Python","C#"]}

for key, values in info2.items():
    if(key.isupper):
        info2[key.lower()] = info2.pop(key)
    
infoDict2 = json.dumps(info2 ,indent=4, sort_keys=True)

print(infoDict2)