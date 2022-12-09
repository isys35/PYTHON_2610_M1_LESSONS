from typing import Union


class Discount:
    def __init__(self, customer: str, price: Union[float, int]):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price


class FavDiscount(Discount):

    def give_discount(self):
        return super().give_discount() * 0.2


class VIPDiscount(Discount):

    def give_discount(self):
        return super().give_discount() * 0.4
