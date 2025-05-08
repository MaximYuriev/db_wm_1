import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class City(Base):
    __tablename__ = "city"
    city_id: Mapped[int] = mapped_column(primary_key=True)
    name_city: Mapped[str]
    days_delivery: Mapped[datetime.datetime]
