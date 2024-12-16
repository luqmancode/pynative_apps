import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{os.path.abspath('pynative.db')}")
Base = declarative_base()
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

