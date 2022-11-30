def generator1(n):
    """

    :param n:
    """
    for i in range(n):
        yield i ** 2
        yield i ** 3
        yield i ** 4


def infiniti_generator():
    """

    """
    a = 0
    while True:
        a += 1
        yield a


def generator_2():
    for i in range(4):
        x = yield i
        print(x)


if __name__ == '__main__':
    # a = generator1(5)
    # print(a)
    # gen = infiniti_generator()
    # print(gen.__next__())
    # print(gen.__next__())
    # print(gen.__next__())
    gen_2 = generator_2()
    print(gen_2)
