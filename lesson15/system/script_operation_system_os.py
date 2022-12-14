import os

print(os.name)

print(os.environ.get("TELEGRAM_TOKEN"))
print(os.getenv("TELEGRAM_TOKEN"))
print(os.getcwd())
# os.mkdir(r"C:\folder")
# os.chdir(r"C:\folder")
# os.rmdir(r"C:\folder")
# os.makedirs(r"C:\folder\folder2\folder3\folder4")
# os.removedirs(r"C:\folder\folder2\folder3\folder4")
# os.startfile(r"C:\del\test.txt")

# with open("name.txt", 'w') as write_file:
#     write_file.write(input("Введите имя:"))

# os.startfile("name.txt")
# os.rename("name.txt", "new_name.txt")

# for file in os.listdir():
#     if file.endswith('.py') and not file.startswith("script"):
#         os.rename(file, f'script_{file}')

# for root, dirs, files in os.walk(r"C:\PYTHON_2610\PYTHON_2610_M1_LESSONS"):
#     for dir in dirs:
#         print(dir)
    # for file in files:
    #     print(file)


# print(os.stat("script_interpritator_sys.py"))

if os.path.exists("dir"):
    os.rmdir("dir")

print(os.path.isfile("name.txt"))

print(os.path.split(__file__))

