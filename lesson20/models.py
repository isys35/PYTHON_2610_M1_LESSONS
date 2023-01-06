from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, PrimaryKeyConstraint, UniqueConstraint, ForeignKeyConstraint, Index, \
    SmallInteger, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('username'),
        UniqueConstraint('email'),
    )


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    content = Column(String(50), nullable=False)
    published = Column(String(200), nullable=False, unique=True)
    user_id = Column(Integer, nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id']),
        Index('title_content_index' 'title', 'content'),
    )


# class Author(Base):
#     __tablename__ = 'authors'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     books = relationship("Book", backref="author")
#
#
# class Book(Base):
#     __tablename__ = 'books'
#     id = Column(Integer, primary_key=True)
#     title = Column(String(100), nullable=False)
#     copyright = Column(SmallInteger, nullable=False)
#     author_id = Column(Integer, ForeignKey('authors.id'))
#     author = relationship("Author", backref="books")


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    designation = Column(String(255), nullable=False)
    doj = Column(Date(), nullable=False)
    dl = relationship('DriverLicense', backref='person', uselist=False)


class DriverLicense(Base):
    __tablename__ = 'driverlicense'
    id = Column(Integer(), primary_key=True)
    license_number = Column(String(255), nullable=False)
    renewed_on = Column(Date(), nullable=False)
    expiry_date = Column(Date(), nullable=False)
    person_id = Column(Integer(), ForeignKey('persons.id'))


# author_book = Table('author_book', Base.metadata,
#                     Column('author_id', Integer(), ForeignKey("authors.id")),
#                     Column('book_id', Integer(), ForeignKey("books.id"))
#                     )


class AuthorBook(Base):
    __tablename__ = 'author_book'
    author_id = Column(Integer(), ForeignKey("authors.id"), primary_key=True)
    book_id = Column(Integer(), ForeignKey("books.id"), primary_key=True)
    book = relationship("Book", backref="authors", uselist=False)
    author = relationship("Author", backref="books", uselist=False)


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship("AuthorBook", backref="author")


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger(), nullable=False)
    author_id = Column(Integer(), ForeignKey('authors.id'))
    authors = relationship("AuthorBook", backref="book")
