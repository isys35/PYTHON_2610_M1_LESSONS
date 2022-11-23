def call_with_five(func):
    return func(5)


def add_one(x):
    return x + 1


def multiply_six(x):
    return x * 6


def double(function):
    def inner(argument):
        return function(argument)
    return inner


if __name__ == '__main__':
    # print(call_with_five(add_one))
    # print(call_with_five(multiply_six))
    inner = double(multiply_six)
    print(inner(10))