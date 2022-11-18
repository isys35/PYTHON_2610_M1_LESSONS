def add_six(list_to_add):
    list_to_add.append(6)


def send_message(name, message):
    print(f"{name}, {message}!")


def greet(*args):
    for arg in args:
        print(arg)


def greet_2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    init_list = [1, 2, 3]
    add_six(init_list)
    print(init_list)
    send_message("Дмитрий", "Здравствуйте")
    send_message(name="Дмитрий", message="Пошёл ВОН!!!")
    send_message(message="Пошёл ВОН!!!", name="Дмитрий")
    send_message("Дмитрий", message="Пошёл ВОН!!!")
    greet("Привет", "Как дела?", "Что делаешь", "Аллллоооооо!!!!")
    greet_2(item_1="Бла Бла", name="Олег")
    example_tuple = ("Один", "Два", "Три", "ABC")
    greet(*example_tuple)
    example_dict = {"name": "Виктор", "surname": "Петров"}
    greet_2(**example_dict)
