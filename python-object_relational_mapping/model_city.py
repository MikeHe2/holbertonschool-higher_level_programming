#!/usr/bin/python3

"""
This module defines the State class, which represents a state in a database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    This class represents a state in a database.

    Attributes:
        id (int): The unique identifier of the state.
        name (str): The name of the state.
    """

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey("states.id"), Integer, nullable=False)