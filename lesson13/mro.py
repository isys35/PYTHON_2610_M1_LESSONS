class A:
    def myname(self):
        print(" I am a class A")


class O:
    def myname(self):
        print(" I am a class O")


class B(O):
    pass


class C(A):
    pass

    # classes ordering


class D(B, C):
    pass


if __name__ == '__main__':
    D().myname()
