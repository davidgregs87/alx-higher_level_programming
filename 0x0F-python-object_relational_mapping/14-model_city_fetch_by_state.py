#!/usr/bin/python3
"""
This module is only meant to print the first line of a query
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_city import Base, City
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

    for cities in session.query(State.name, City.id, City.name)\
            .filter(City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(cities[0], cities[1], cities[2]))
    # Session closed
    session.close()
