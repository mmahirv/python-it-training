from functools import reduce

names = lambda first, last: f"{first} {last}"

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'pear', 'plum', 'strawberry', 'watermelon']

sorted_fruits = sorted(fruits, key=lambda x: len(x))

print(sorted_fruits)

print(reduce(names, fruits))

names_people = ['Charlie', 'alice', 'Bob', 'David', 'Eve', 'frank', 'Grace', 'Heidi', 'ivan', 'Judy']

print(sorted(names_people))

items = ['3', 'a', 'B', '2', 'c', 'C', '1', 'd', 'D', 'A']

print(sorted(items, key=lambda x: (not x.isdigit(), x.lower(), x.isupper())))