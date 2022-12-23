from openpyxl import Workbook

wb = Workbook()

DATA = list(range(1, 20))


ws = wb.active
ws.title = "Первая страница"

for i in DATA:
    ws.cell(i, 1, i)

wb.save('test.xlsx')




print(ws)