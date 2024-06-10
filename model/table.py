from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Vehicles(Base):
    __tablename__ = "vehicles"

    id = Column("id", Integer, primary_key=True)
    make = Column("make", String(50))
    model = Column("model", String(50))
    year = Column("year", Integer())
    color = Column("color", String(50))

