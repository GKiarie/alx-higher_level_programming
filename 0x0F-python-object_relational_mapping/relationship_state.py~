#!/usr/bin/python3
"""python file that contains the class definition
of a State and an instance Base = declarative_base()
"""


from sqlalchemy import MetaData, Table, Integer, String, \
    Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """ A State Class Definition"""
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
