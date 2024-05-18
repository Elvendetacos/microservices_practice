from sqlalchemy import String, Column, Table, Integer, ForeignKey
from infraestructure.configuration.db import Base, engine, meta
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'
    id = Column(String(255), primary_key=True, unique=True)
    name = Column(String(100))
    price = Column(Integer)
    stock = Column(Integer)


Base.metadata.create_all(engine)
