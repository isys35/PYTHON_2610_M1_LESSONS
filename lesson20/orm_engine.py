from sqlalchemy import create_engine

# 1111 это мой пароль для пользователя postgres
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost/sqlalchemy_tuts",
    echo=True
)
engine.connect()

print(engine)

