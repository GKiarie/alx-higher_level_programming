#!/usr/bin/python3
"""script that adds State object "Louisiana"
to the database h0btn_0e_6_usa"""
from model_state import Base, State
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
    state_to_add = State(name="Louisiana")
    session.add(state_to_add)
    session.commit()
    q = session.query(State).filter(State.name == "Louisiana").first()

    print(f'{q.id}')
    session.close()
