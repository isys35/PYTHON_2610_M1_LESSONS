from functools import reduce

# def double(x):
#     return x*2

if __name__ == '__main__':
    # double = lambda x: x*2
    # print(double(2))
    my_list = [1, 4, 7, 12, 13, 53, 12, 54]
    result = list(filter(lambda x: x % 2 == 0, my_list))
    print(result)

    result_map = list(map(lambda x: x*2, my_list))
    print(result_map)

    result_reduce = reduce(lambda x, y: x*y, my_list)
    print(result_reduce)

    sequence = [
        {'key': 12},
        {'key': 32},
        {'key': 17}
    ]

    sequence.sort(key=lambda x: x["key"])
    print(sequence)

