#!/usr/bin/python3
"""python file that contains the class definition
of a State and an instance Base = declarative_base()
"""


from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ A State Class Definition"""
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
