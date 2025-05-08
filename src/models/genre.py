from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Genre(Base):
    __tablename__ = "genre"
    genre_id: Mapped[int] = mapped_column(primary_key=True)
    name_genre: Mapped[str]
