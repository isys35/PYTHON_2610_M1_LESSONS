from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from lesson21.alchemy.models import Order
from lesson21.alchemy.orm_engine import engine

session = Session(bind=engine)


def dispatch_order(order_id):
    # проверка того, правильно ли указан order_id
    order = session.query(Order).get(order_id)

    if not order:
        raise ValueError("Недействительный order_id: {}.".format(order_id))

    try:
        for order_line in order.line_items:
            order_line.item.quantity = order_line.item.quantity - order_line.quantity

        order.date_placed = datetime.now()
        session.commit()
        print("Транзакция завершена.")

    except IntegrityError as e:
        print(e)
        print("Возврат назад...")
        session.rollback()
        print("Транзакция не удалась.")


if __name__ == '__main__':
    dispatch_order(1)
