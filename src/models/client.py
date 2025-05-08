from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.models.city import City


class Client(Base):
    __tablename__ = "client"
    client_id: Mapped[int] = mapped_column(primary_key=True)
    name_client: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey(City.city_id))
    email: Mapped[str]
