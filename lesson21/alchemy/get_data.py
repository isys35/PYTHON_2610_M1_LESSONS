from sqlalchemy import or_, desc, func, cast, Integer, Numeric, DateTime, Date
from sqlalchemy.orm import Session

from lesson21.alchemy.models import Customer, Item, Order
from lesson21.alchemy.orm_engine import engine

session = Session(bind=engine)

# print(session.query(Customer.id, Customer.first_name))
# customers = session.query(Customer.id, Customer.first_name).all()
# print(customers)


# q = session.query(Customer)
#
# for c in q:
#     print(c.id, c.first_name)

# COUNT(*)
print(session.query(Item).count())

# LIMIT 1
print(session.query(Item).first())

# WHERE id = %(param)s
print(session.query(Customer).get(1))

# WHERE first_name='Dmitriy'
print(session.query(Customer).filter(Customer.first_name == "Dmitriy").all())

# WHERE first_name='Dmitriy' AND last_name='Yatsenko'
print(session.query(Customer).filter(
    Customer.first_name == "Dmitriy", Customer.last_name == "Yatsenko"
).all())

# WHERE first_name LIKE 'V%'
print(session.query(Customer.id, Customer.first_name).filter(
    Customer.first_name.like("V%")
).all())

# WHERE first_name = 'Dmitriy' OR first_name = 'Valeriy'
print(session.query(Customer.id, Customer.first_name).filter(
    or_(Customer.first_name == "Dmitriy", Customer.first_name == "Valeriy")
).all())

# WHERE date_placed IS NULL
print(session.query(Order).filter(Order.date_placed == None).all())

# WHERE date_placed IS NOT NULL
print(session.query(Order).filter(Order.date_placed != None).all())

# WHERE first_name IN ('Dmitriy', 'Valeriy')
print(session.query(Customer.id, Customer.first_name).filter(
    Customer.first_name.in_(['Dmitriy', 'Valeriy'])
).all())

# WHERE first_name NOT IN ('Dmitriy', 'Valeriy')
print(session.query(Customer.id, Customer.first_name).filter(
    Customer.first_name.notin_(['Dmitriy', 'Valeriy'])
).all())

# WHERE name ILIKE 'w%'
print(session.query(Item).filter(Item.name.ilike("w%")).all())

# WHERE first_name='Dmitriy' LIMIT 2
print(session.query(Customer).filter(Customer.first_name == 'Dmitriy').limit(2).all())

# WHERE first_name='Dmitriy' LIMIT 2 OFFSET 2
print(session.query(Customer).filter(Customer.first_name == 'Dmitriy').limit(2).offset(2).all())

# ORDER BY cost_price
print(session.query(Item.id, Item.name, Item.cost_price).order_by(Item.cost_price).all())

# ORDER BY cost_price DESC
print(session.query(Item.id, Item.name, Item.cost_price).order_by(desc(Item.cost_price)).all())

# FROM customers JOIN orders ON customers.id = orders.customer_id
print(session.query(Customer).join(Order).all())

# FROM customers JOIN orders ON customers.id = orders.customer_id
print(session.query(Customer.id, Customer.username, Order.id).join(Order).all())

# FROM customers LEFT OUTER JOIN orders ON customers.id = orders.customer_id
print(session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order).all())

# FROM customers GROUP BY first_name
print(
    session.query(Customer.first_name, func.count()).group_by(Customer.first_name).all()
)

# FROM customers GROUP BY first_name HAVING count(*) > 4
print(
    session.query(Customer.first_name, func.count()).group_by(Customer.first_name).having(func.count() > 4).all()
)

# SELECT DISTINCT first_name FROM customers
print(session.query(Customer.first_name).distinct().all())


# SELECT CAST(pi() AS INTEGER),
#   CAST(pi() AS NUMERIC(10, 2)),
#   CAST('2010-12-01' AS TIMESTAMP WITHOUT TIME ZONE),
#   CAST('2010-12-01' AS DATE)
print(session.query(
    cast(func.pi(), Integer),
    cast(func.pi(), Numeric(10,2)),
    cast("2010-12-01", DateTime),
    cast("2010-12-01", Date),
).all())

# SELECT id, first_name FROM customer
#  UNION
# SELECT id, name FROM items;
s1 = session.query(Customer.id, Customer.first_name)
s2 = session.query(Item.id, Item.name)
print(s1.union(s2).all())