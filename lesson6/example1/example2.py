command = input("Введите направление:")
match command:
    case "прямо":
        print("Вы пошли прямо и потеряли коня")
    case "налево":
        print("Вы пошли налево и нашли принцесу для коня")
    case "направо":
        print("Вы пошли направо и попали в IT")
    case _:
        print("Пока!")

command = input("Введите направление:")
if command == "прямо":
    print("Вы пошли прямо и потеряли коня")
elif command == "налево":
    print("Вы пошли налево и нашли принцесу для коня")
elif command == "направо":
    print("Вы пошли направо и попали в IT")
else:
    print("Пока!")