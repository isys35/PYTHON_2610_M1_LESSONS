import multiprocessing


def worker(index):
    """Рабочая функция"""
    print(f'Worker {index}')


if __name__ == '__main__':
    for index in range(5):
        p = multiprocessing.Process(target=worker, args=(index,))
        p.start()
