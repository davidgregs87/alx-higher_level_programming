#!/usr/bin/python3
"""script that lists all State objects that contain the letter a from the
   database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    for state in session.query(State).order_by(State.id).\
            filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))

    session.close()
