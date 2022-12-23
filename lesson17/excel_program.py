import datetime

from openpyxl.workbook import Workbook

XLSX_FILE_NAME = "calculate_result.xlsx"


def get_info_from_user():
    a = int(input("Введите число а: "))
    b = int(input("Введите число b: "))
    result = a + b
    print(result)
    return a, b, result


def append_calculate_data(data: list):
    a, b, result = get_info_from_user()
    result_date = datetime.datetime.now()
    result_date_str = result_date.strftime("%H:%M:%S")
    data.append([result_date_str, a, b, result])


def write_xlsx(data: list):
    wb = Workbook()
    ws = wb.active
    for row in data:
        ws.append(row)
    wb.save(XLSX_FILE_NAME)


if __name__ == '__main__':
    data = [["Время", "a", "b", "Сумма"]]
    while True:
        try:
            append_calculate_data(data)
        except ValueError:
            break

        if input("Выйти (y,n)?") == "y":
            break
    try:
        write_xlsx(data)
    except PermissionError:
        input("Закройте excel и нажмите Enter:")
