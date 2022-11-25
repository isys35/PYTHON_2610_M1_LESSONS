import time


def repeat(count):
    def decorator(func):
        def inner(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)

        return inner

    return decorator


def counter_slow():
    count = 0

    def decorator(func):
        def inner(*args, **kwargs):
            nonlocal count
            func(*args, **kwargs)
            count += 1
            print(count)
            time.sleep(1)

        return inner

    return decorator
