#!/usr/bin/python3
"""
A module that defines a class called State
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Returns a class object
Base = declarative_base()


class State(Base):
    """
    A class State, that would represents a table called state
    """
    # The name of the table is called states
    __tablename__ = 'states'

    # We then add columns
    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
