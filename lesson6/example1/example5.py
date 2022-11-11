week = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье",
}

number = int(input("Введите число: "))
# print(week[number])
if week_name := week.get(number):
    print(week_name)
else:
    print("АААААА не работает!!!")
