my_list = ['a', 'b', 'c', 'd', 'd', 'd', 'e', 'f']
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

print(my_list)
print(my_dict)

print(len(my_list))
print(len(my_dict))

print('a' in my_list)
print('g' not in my_list)

# Проверяет в ключах
print('a' in my_dict)
print('a' in my_dict.keys())

# Проверяет в значениях словаря
print(4 in my_dict.values())

# Проверяем наличие пар
print(('c', 3) in my_dict.items())

for item in my_list:
    print(item)

for item in my_dict:
    print(item)

for key, value in my_dict.items():
    print(key, value)

# min(), max(), sum()

# Кол-во 'a'
my_list.count('a')

print(my_list.index('d'))

