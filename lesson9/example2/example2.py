message_1 = 'Глобальная переменная'
list_example = [0, 1, 2]
count = 0


def func():
    print("Мы внутри функции")
    list_example.append(3)
    print(message_1)
    global count
    count = count + 1
    message_2 = "Локальная переменная"
    print(message_2)


if __name__ == '__main__':
    func()
    print(message_1)
    print(list_example)
    print(count)
