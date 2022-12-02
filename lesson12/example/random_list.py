import random


class Random:

    def __init__(self, list_len, item_max_size=100):
        self.__list_len = list_len
        self.__item_max_size = item_max_size

    def __iter__(self):
        return RandomIterator(self.__list_len, self.__item_max_size)


class RandomIterator:

    def __init__(self, list_len, item_max_size):
        self.__step = 0
        self.__list_len = list_len
        self.__item_max_size = item_max_size

    def __next__(self):
        if self.__step == self.__list_len:
            raise StopIteration
        self.__step += 1
        return random.randint(0, self.__item_max_size)



if __name__ == '__main__':
    random_list = list(Random(100))
    for i in Random(100):
        print(i)
    print(random_list)