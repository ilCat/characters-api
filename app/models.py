from sqlalchemy.orm import Mapped, mapped_column

# from app.models.base import SQLModel


class CharacterModel:  # (SQLModel):
    __tablename__ = "characters"
    __table_args__ = {"schema": "pidemo"}

    id: Mapped[int] = mapped_column("id", primary_key=True, unique=True)
    name: Mapped[str] = mapped_column("name")
    height: Mapped[int] = mapped_column("height")
    mass: Mapped[int] = mapped_column("mass")
    hair_color: Mapped[str] = mapped_column("hair_color")
    skin_color: Mapped[str] = mapped_column("skin_color")
    eye_color: Mapped[str] = mapped_column("eye_color")
    birth_year: Mapped[int] = mapped_column("birth_year")
