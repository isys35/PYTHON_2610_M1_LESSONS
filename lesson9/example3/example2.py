from lesson9.example3.decorators import brenchmark


@brenchmark
def func1():
    count = 0
    items = [1, 2, 3]

    def inner():
        nonlocal count
        print(count)
        print(items)
        items.append(4)
        print(items)
        count += 1
        print(count)

    return inner


if __name__ == '__main__':
    inner = func1()
    inner()