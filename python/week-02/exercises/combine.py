#numbers = list(range(1, 11))

#squared_numbers = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

#print(squared_numbers)

list1 = ['1','two','4x']

digits = filter(lambda x: x.isdigit(),list1)

int_digits = list(map(lambda x: int(x), digits))

print(int_digits)