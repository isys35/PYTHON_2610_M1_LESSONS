class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        super().__init__(l, w, h)
        self.places = p


class DeskTable(Table):
    def square(self):
        return self.width * self.length


# class ComputerTable(DeskTable):
#     def square(self, monitor=0.0):
#         return self.width * self.length - monitor


class ComputerTable(DeskTable):
    def square(self, monitor=0.0):
        return super().square() - monitor

t1 = Table(1.5, 1.8, 0.75)

t2 = DeskTable(0.8, 0.6, 0.7)
t3 = ComputerTable(1.5, 1.8, 0.75)
print(t3.square(monitor=0.6))
t4 = KitchenTable(1.5, 1.8, 0.75, 4)
print(t4.places)