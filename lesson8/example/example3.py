try:
    raise IndexError # Генерация исключения вручную
except IndexError:
    print('got exception') # Получено исключение