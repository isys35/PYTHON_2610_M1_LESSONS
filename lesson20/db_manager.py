from lesson20.models import Base
from lesson20.orm_engine import engine
import sys


if __name__ == '__main__':
    if sys.argv[1] == "create_all":
        Base.metadata.create_all(engine)
    elif sys.argv[1] == "drop_all":
        Base.metadata.drop_all(engine)