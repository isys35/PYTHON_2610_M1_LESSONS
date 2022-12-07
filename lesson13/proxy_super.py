class Base:
    def price(self):
        return 10


class Big(Base):
    def price(self):
        return super().price() * 1.1


class Discount(Big):
    def price(self):
        return super().price() * .8


class O:
    def method(self):
        print('I am O')


class A(O):
    def method(self):
        super().method()
        print('I am A')


class B(O):
    def method(self):
        super().method()
        print('I am B')


class C(A, B):
    def method(self):
        super().method()
        print('I am C')


if __name__ == '__main__':
    # discount = Discount()
    # print(super(Discount, discount).price())
    # print(discount.price())
    C().method()
    print(C.__mro__)
    print()
