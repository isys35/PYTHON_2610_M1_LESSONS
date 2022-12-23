import csv

import pandas
import pandas as pd

DATA = [
   ['Имя', 'Пол', 'Возраст'],
   ['Алексей', 'муж.', '20'],
   ['Алина', 'жен.', '21'],
]


_csv = ''
for row in DATA:
    _csv += ';'.join(row) + '\n'

# with open("test.csv", "w", encoding="utf-8") as csv_file:
#     csv_file.write(_csv)

CSV_KWARGS = {
    "delimiter": ';',
    "skipinitialspace": True
}

# csv.register_dialect("CSVDialect", delimiter=';', skipinitialspace=True)

with open("test.csv", "r", encoding="utf-8") as csv_file:
    data = csv.reader(csv_file, **CSV_KWARGS)
    for row in data:
        for cell in row:
            print(cell)


with open("test.csv", "r", encoding="utf-8") as csv_file:
    data = csv.DictReader(csv_file, **CSV_KWARGS)
    for row in data:
        print(row)


csv_pand_file = pandas.read_csv("test.csv", delimiter=";")
print(csv_pand_file)


DATA_2 = [
   ['Имя', 'Пол', 'Возраст', 'Професия'],
   ['Алексей', 'муж.', '20', "Инженер"],
   ['Алина', 'жен.', '21', "Тракторист"],
]

DATA_3 = [
    {"имя": "Игорь", "фамилия": "Петров"},
    {"имя": "Витя", "фамилия": "Калинин"},
]

with open("test_2.csv", "w", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    # writer.writerows(DATA_2)
    for line in DATA_2:
        writer.writerow(line)


with open("test_3.csv", "w", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=["имя", "фамилия"])
    writer.writerows(DATA_3)



data_frame_1 = pd.DataFrame(DATA_3)

data_frame_1.to_csv("test_4.csv", sep=";")
