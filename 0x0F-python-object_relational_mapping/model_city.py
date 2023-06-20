#!/usr/bin/python3
"""
A module that contains a definition of class
called City
"""
from model_state import Base, State
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    A class called City
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
