#!/usr/bin/python3
"""script that creates the State “California” with the City “San Francisco”
   from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    add_state = State(name='California')
    add_city = City(name='San Francisco', state=add_state)
    # add_state.state = [City(name='San Francisco')]
    session.add(add_city)
    session.commit()

    session.close()
