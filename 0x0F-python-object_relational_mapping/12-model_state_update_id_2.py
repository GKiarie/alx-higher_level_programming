#!/usr/bin/python3
"""script that chamnges name 0f State object
in the database h0btn_0e_6_usa"""
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
    session.query(State).filter(State.id == 2).\
        update({"name": "New Mexico"}, synchronize_session='fetch')
    session.commit()
    session.close()
