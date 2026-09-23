l1 = [1, 2, 3, 4, 5]  # 5 elemanlı
l2 = [10, 20]         # 2 elemanlı

sonuc = list(map(lambda x, y: x + y, l1, l2))
print(sonuc) 