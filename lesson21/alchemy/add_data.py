from sqlalchemy.orm import Session

from lesson21.alchemy.models import Customer, Item, Order, OrderLine
from lesson21.alchemy.orm_engine import engine

session = Session(bind=engine)

c1 = Customer(
    first_name='Dmitriy',
    last_name='Yatsenko',
    username='Moseend',
    email='moseend@mail.com'
)

c2 = Customer(
    first_name='Valeriy',
    last_name='Golyshkin',
    username='Fortioneaks',
    email='fortioneaks@gmail.com'
)

# session.add(c1)
# session.add(c2)

session.add_all([c1, c2])

print(session.new)

c3 = Customer(
    first_name="Vadim",
    last_name="Moiseenko",
    username="Antence73",
    email="antence73@mail.com",
)

c4 = Customer(
    first_name="Vladimir",
    last_name="Belousov",
    username="Andescols",
    email="andescols@mail.com",
)

c5 = Customer(
    first_name="Tatyana",
    last_name="Khakimova",
    username="Caltin1962",
    email="caltin1962@mail.com",
)

c6 = Customer(
    first_name="Pavel",
    last_name="Arnautov",
    username="Lablen",
    email="lablen@mail.com",
)

session.add_all([c4, c5, c6])

i1 = Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = Item(name='Pen', cost_price=3.45, selling_price=4.51, quantity=3)
i3 = Item(name='Headphone', cost_price=15.52, selling_price=16.81, quantity=50)
i4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = Item(name='Keyboard', cost_price=20.1, selling_price=22.11, quantity=50)
i6 = Item(name='Monitor', cost_price=200.14, selling_price=212.89, quantity=50)
i7 = Item(name='Watch', cost_price=100.58, selling_price=104.41, quantity=50)
i8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()

o1 = Order(customer=c1)
o2 = Order(customer=c1)

line_item1 = OrderLine(order=o1, item=i1, quantity=3)
line_item2 = OrderLine(order=o1, item=i2, quantity=2)
line_item3 = OrderLine(order=o2, item=i1, quantity=1)
line_item4 = OrderLine(order=o2, item=i2, quantity=4)

session.add_all([o1, o2])

o3 = Order(customer=c1)
orderline1 = OrderLine(item=i1, quantity=5)
orderline2 = OrderLine(item=i2, quantity=10)

o3.line_items.append(orderline1)
o3.line_items.append(orderline2)

session.commit()

print(c1.id)
print(c2.id)

# print(c1.orders, c2.orders)
