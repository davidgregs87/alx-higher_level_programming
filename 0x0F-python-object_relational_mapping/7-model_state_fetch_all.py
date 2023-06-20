#!/usr/bin/python3
"""
List all states
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

# Makes this script not importable in another file
if __name__ == '__main__':

    # Create new engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[1],
                                   sys.argv[3]), pool_pre_ping=True)

    # imports all metadata to be available in the engine
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    for states in session.query(State).order_by(State.id).all():
        print('{}: {}'.format(states.id, states.name))

    # Close session
    session.close()
