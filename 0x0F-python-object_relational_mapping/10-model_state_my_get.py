#!/usr/bin/python3
"""
This module is only meant to print the first line of a query
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State

# Now let's set-up connection to a database
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Let's begin session

    Session = sessionmaker(bind=engine)

    session = Session()

    # Let's now begin query

    info = session.query(State).filter(State.name == (sys.argv[4],))
    for x in info:
        if not (x):
            print('Not found')
        else:
            print('{}'.format(x.id))

    # Session closed
    session.close()
