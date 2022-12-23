NAME_FILE = "test.txt"

# init_text = input("Введите текст для записи в файл: ") + '\n'
# init_text = init_text * 1000

# file = open(NAME_FILE, mode="w", encoding="utf-8")
# file.write(init_text)
# file.close()

# with open(NAME_FILE, "r", encoding="utf-8") as file:
#     for line in file:
#         print(line)

# with open(NAME_FILE, "a", encoding="utf-8") as file:
#     print(5, file=file)
    # file.write(str(5))


with open(NAME_FILE, "rb") as file:
    a = file.read()
    print(a)






