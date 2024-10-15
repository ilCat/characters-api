from sqlalchemy import create_engine

from app.models.character import Base
from sqlalchemy.orm import Session
from .util import create_bd_file
import os

folder = os.environ.get("VOLUME_NAME", "db_data")
os.chdir("..")
path = os.getcwd()

create_bd_file(folder, "./")

# Crear una instancia de motor SQLite
engine = create_engine(f"sqlite:///{folder}/sqlitedb.db")

# Crear una instancia DeclarativeMetals
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
