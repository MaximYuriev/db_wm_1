from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.models.client import Client


class Buy(Base):
    __tablename__ = "buy"
    buy_id: Mapped[int] = mapped_column(primary_key=True)
    buy_description: Mapped[str]
    client_id: Mapped[int] = mapped_column(ForeignKey(Client.client_id))
