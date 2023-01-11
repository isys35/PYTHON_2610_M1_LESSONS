from sqlalchemy.orm import Session

from lesson21.alchemy.models import Item
from lesson21.alchemy.orm_engine import engine

session = Session(bind=engine)

pen = session.query(Item).get(2)
pen.selling_price = 9.99

session.add(pen)

# UPDATE items SET selling_price='9.99' WHERE items.id = 2
session.commit()

# DELETE FROM items WHERE item.name = 'Monitor' LIMIT 1
monitor = session.query(Item).filter(Item.name == 'Monitor').first()
session.delete(monitor)
session.commit()

# DELETE FROM items WHERE items.name ='Monitor'
session.query(Item).filter(Item.name == 'Monitor').delete(synchronize_session='fetch')
session.commit()