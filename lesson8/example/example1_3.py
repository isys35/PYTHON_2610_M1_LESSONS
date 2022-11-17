list_1 = [1, 2, 3]

try:
    input_index = int(input("Введите индекс: "))
    value = list_1[input_index]
except IndexError:
    print("Индекса нету в списке!")
else:
    print(value)