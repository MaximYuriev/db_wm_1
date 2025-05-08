import decimal

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.author import Author
from src.models.base import Base
from src.models.genre import Genre


class Book(Base):
    __tablename__ = "book"
    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey(Author.author_id))
    genre_id: Mapped[int] = mapped_column(ForeignKey(Genre.genre_id))
    price: Mapped[decimal.Decimal]
    amount: Mapped[int]
