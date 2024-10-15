# from sqlalchemy.orm import Mapped, Column
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase


class Base(DeclarativeBase):
    pass


class CharacterModel(Base):
    __tablename__ = "characters"
    # __table_args__ = {"schema": "pidemo"}

    id = Column(Integer, name="id", primary_key=True)
    name = Column(String, name="name")
    height = Column(Float, name="height")
    mass = Column(Float, name="mass")
    hair_color = Column(String, name="hair_color")
    skin_color = Column(String, name="skin_color")
    eye_color = Column(String, name="eye_color")
    birth_year = Column(Integer, name="birth_year")
