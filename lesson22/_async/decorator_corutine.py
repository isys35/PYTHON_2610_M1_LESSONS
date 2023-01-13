def coroutine(func):
    def wrapper(*args, **kwargs):
        cor = func(*args, **kwargs)
        next(cor)
        return cor

    return wrapper


@coroutine
def simple_coroutine():
    print("Я корутина")
    try:
        while True:
            value = yield
            print(value)
    except GeneratorExit:
        print("Exiting coroutine...")


### Конвеер

def producer(cor):
    n = 1
    while n < 100:
        cor.send(n)
        n = n * 2


@coroutine
def my_filter(num, cor):
    while True:
        n = yield
        if n < num:
            cor.send(n)


@coroutine
def printer():
    while True:
        n = yield
        print(n)


if __name__ == '__main__':
    # cor = simple_coroutine()
    # cor.send("Значение 1")
    # cor.send("Значение 2")
    prnt = printer()
    filt = my_filter(50, prnt)
    producer(filt)
