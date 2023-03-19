#!/usr/bin/python3
"""script that lists all State & City objects
from the database h0btn_0e_6_usa"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(City.name, City.id, State.name).join(State).all()

    for row in q:
        print(f'{row[2]}: ({row[1]}) {row[0]}')
    session.close()
