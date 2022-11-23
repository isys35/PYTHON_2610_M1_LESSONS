import time


def brenchmark(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f'[INFO] {func.__name__} Выполнилась за {end_time:.5f} секунд')
        return result
    return wrapper
