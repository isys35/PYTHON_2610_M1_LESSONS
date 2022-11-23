from lesson9.example3.decorators import brenchmark
import random


@brenchmark
def sort_bubble(mas):
    k = len(mas)
    flg = 1
    while (flg):
        flg = 0
        for i in range(k):
            if mas[i] % 2 != 0:
                for j in range(i, k):
                    if (mas[j] % 2 == 1) & (mas[j] < mas[i]):
                        flg = 1
                        mas[i], mas[j] = mas[j], mas[i]


@brenchmark
def odd_items(numbers_list):
    odds = sorted([i for i in numbers_list if i % 2 != 0], reverse=True)
    return [odds.pop() if i % 2 != 0 else i for i in numbers_list]


mas = []
for i in range(10000):
    mas.append(random.randint(0, 1000))
mas_2 = odd_items(mas.copy())
print(mas_2)

mas_1 = mas.copy()
sort_bubble(mas_1)
print(mas_1)

print(mas_1 == mas_2)

