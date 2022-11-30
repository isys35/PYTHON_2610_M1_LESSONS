import random
import time


class Coin:

    def __init__(self):
        self.__sideup = 'Орел'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    def get_sideup(self):
        return self.__sideup


if __name__ == '__main__':

    coin = Coin()
    coin_2 = Coin()
    print(coin._Coin__sideup)
    # coin.toss()
    # Coin.toss(coin)
    # print(coin.get_sideup())