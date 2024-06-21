#!/usr/bin/python3

"""
This script fetches the first state from the database
and prints its ID and name.
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    if session.query(State) is None:
        print()

    state_id = session.query(State).first().id
    state_name = session.query(State).first().name
    print("{}: {}".format(state_id, state_name))

    session.close()
