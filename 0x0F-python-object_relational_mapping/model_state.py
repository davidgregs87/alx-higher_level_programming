#!/usr/bin/python3
"""
State model with SqlAchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ class definition of a State and an instance Base = declarative_base """
    __tablename__ = 'states'
    # autoincrement=True is auto populated
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
