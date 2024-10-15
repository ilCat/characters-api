from sqlalchemy import create_engine

from app.models.character import Base
from sqlalchemy.orm import Session
from .util import create_bd_file
import os

folder = os.environ.get("VOLUME_NAME", "db_data")
os.chdir("..")
path = os.getcwd()

create_bd_file(folder, "./")

# Create engine instace
engine = create_engine(f"sqlite:///{folder}/sqlitedb.db")

# Create  tables from Base
base = Base()
base.metadata.create_all(engine)
