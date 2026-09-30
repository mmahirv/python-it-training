import sum_module

def carp(a,b):
    print('Main fonksiyon')
    sum_module.topla(a,b)
    return a * b

sum_module.topla(1,2)

if __name__ == "__main__":
    print(carp(int(input('Enter fact nummer: ')), int(input('Enter fact nummer: '))))
    
sum_module.topla(34,3)