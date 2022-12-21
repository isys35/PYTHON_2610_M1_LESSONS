def upper_decorator(func):
    def wrapper():
        result = func()
        return result.upper() * 3

    return wrapper


@upper_decorator
def say_hi():
    return 'hello world'


@upper_decorator
def say_gaf():
    return 'Гав!'


if __name__ == '__main__':
    # say_hi = upper_decorator(say_hi)
    # print(say_hi())
    print(say_hi())
    print(say_gaf())
