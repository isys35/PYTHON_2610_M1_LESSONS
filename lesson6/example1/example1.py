number = int(input("Введите число"))

if number > 10 or number > 14:
    print("Число больше 10")
elif number == 5:
    print("Число равно 5")
else:
    print("Не подходит не под одно условие")


x = 1
if x:
    y = 2
    if y:
        print('block2')
    print('block1')
print('blockO')


variable = input("Введите число:") or input("Ну пожалуйста! Введите число:")
print(variable)