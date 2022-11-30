"""
    Домашние задание №1

    Описание задачи
"""

from statistics import mean


def mean_min_mas(*num):
    """
    Описание функции

    :param num: Произвольное число аргументов
    :return: [Минимум, Максимум, Среднее]
    """
    return [min(num), max(num), mean(num)]



if __name__ == '__main__':
    new_list = mean_min_mas(1, 2, 4, 0, -5, 5, 8, 9, 7, 6)
    print(new_list)