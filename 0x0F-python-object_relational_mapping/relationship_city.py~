#!/usr/bin/python3
"""python file that contains the class definition
of a City and an instance Base = declarative_base()
"""


from sqlalchemy import MetaData, Table, Integer, String, \
    Column, ForeignKey
from model_state import Base, State


class City(Base):
    """ A City Class Definition"""
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'))
