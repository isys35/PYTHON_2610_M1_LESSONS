NOW = 2022

name = input("Введите имя: ").capitalize()
surname = input("Введите фамилию: ").capitalize()

hello = f"Добро пожаловать, {name} {surname}!"

print(hello)

birthday = int(input("Введите год вашего рождения: "))

user_age = f"Вам {NOW - birthday} лет!"

print(user_age)

year_salary = float(input("Введите годовой доход: "))

month_salary = f"Ваш ежемесячный доход: {year_salary/12:15,.0f}"

print(month_salary)

super_result = "Имя: {0}, Фамилия: {1}".format(name, surname)
super_result_2 = "Ваш год рождения: {year}".format(year=birthday)
print(super_result)
print(super_result_2)
input("Введите Enter...")