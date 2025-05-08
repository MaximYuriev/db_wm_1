import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.models.buy import Buy
from src.models.step import Step


class BuyStep(Base):
    __tablename__ = "buy_step"
    buy_step_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey(Buy.buy_id))
    step_id: Mapped[int] = mapped_column(ForeignKey(Step.step_id))
    data_seq_beg: Mapped[datetime.datetime]
    data_seq_end: Mapped[datetime.datetime]
