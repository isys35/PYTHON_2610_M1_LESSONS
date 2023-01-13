def filter_line(num):
    while True:
        line = yield
        if num in line:
            print(line)


cor = filter_line("33")
next(cor)
cor.send("Jessica, age:24")
cor.send("Marco, age:33")
cor.send("Filipe, age:55")


def joint_print():
    while True:
        part_1 = yield
        part_2 = yield
        print("{} {}".format(part_1, part_2))


cor = joint_print()
next(cor)
cor.send("So Far")
cor.send("So Good")


def test():
    while True:
        value = yield
        print(value)


try:
    cor = test()
    next(cor)
    cor.close()
    cor.send("So Good")
except StopIteration:
    print("Done with the basics")
