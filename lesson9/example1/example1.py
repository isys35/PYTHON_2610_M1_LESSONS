from statistics import mean


def get_indicators(*args):
    return min(args), max(args), mean(args)


def get_indicators_high(*funcs):
    def inner(*args):
        return [func(args) for func in funcs]
    return inner


if __name__ == '__main__':
    min1, max1, mean1 = get_indicators(1, 4, 11, 42, 43, 12, 5, 6)
    min2, max2, mean2 = get_indicators(4, 10, 2, 3, 0, 2, 55, 73)
    min3, max3, mean3 = get_indicators(31, 8, 16, 25, 43, 12, 10)
    assert min1 == 1, "Ошибка"
    assert max1 == 43, "Ошибка"
    assert mean1 == 15.5, "Ошибка"
    assert min2 == 0, "Ошибка"
    assert max2 == 73, "Ошибка"
    assert mean2 == 18.625, "Ошибка"
    assert min3 == 8, "Ошибка"
    assert max3 == 43, "Ошибка"
    assert mean3 == 20.714285714285715, "Ошибка"

    min1, max1, mean1 = get_indicators_high(min, max, mean)(1, 4, 11, 42, 43, 12, 5, 6)
    min2, max2, mean2 = get_indicators_high(min, max, mean)(4, 10, 2, 3, 0, 2, 55, 73)
    min3, max3, mean3 = get_indicators_high(min, max, mean)(31, 8, 16, 25, 43, 12, 10)
    inner = get_indicators_high(min, max, mean)
    print(inner(31, 8, 16, 25, 43, 12, 10))
    assert min1 == 1, "Ошибка"
    assert max1 == 43, "Ошибка"
    assert mean1 == 15.5, "Ошибка"
    assert min2 == 0, "Ошибка"
    assert max2 == 73, "Ошибка"
    assert mean2 == 18.625, "Ошибка"
    assert min3 == 8, "Ошибка"
    assert max3 == 43, "Ошибка"
    assert mean3 == 20.714285714285715, "Ошибка"
