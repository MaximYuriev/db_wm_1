from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.models.book import Book
from src.models.buy import Buy


class BuyBook(Base):
    __tablename__ = "buy_book"
    buy_book_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey(Buy.buy_id))
    book_id: Mapped[int] = mapped_column(ForeignKey(Book.book_id))
    amount: Mapped[int]
