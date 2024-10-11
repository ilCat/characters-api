from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear una instancia de motor SQLite
motor = create_engine("sqlite:///fastapidb.db")

# Crear una instancia DeclarativeMeta
Base = declarative_base()

# Crear la clase SessionLocal desde el factory sessionmaker
SesionLocal = sessionmaker(bind=motor, expire_on_commit=False)
