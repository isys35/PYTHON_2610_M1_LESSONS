from lesson9.example3.decorators import brenchmark


@brenchmark
def example_func(list1, list2, list3):
    for item_1 in list1:
        for item_2 in list2:
            for item_3 in list3:
                print(item_1, item_2, item_3)


if __name__ == '__main__':
    example_func(range(10), range(10), range(10))
