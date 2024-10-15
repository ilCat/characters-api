from sqlalchemy import create_engine

from app.models.character import Base
from sqlalchemy.orm import sessionmaker, Session
from .util import create_bd_file

create_bd_file(".dataLite", "./")

# Crear una instancia de motor SQLite
engine = create_engine("sqlite:///.dataLite/challengedb.db")

# Crear una instancia DeclarativeMeta
base = Base()
base.metadata.create_all(engine)

# Crear la clase session desde el factory sessionmaker
session = Session(engine)
# Session()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close
