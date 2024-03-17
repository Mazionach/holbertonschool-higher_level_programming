#!/usr/bin/python3

"""
Script to delete a state from database
using SQLAlchemy
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}")

    sescla = sessionmaker(bind=engine)

    session = sescla()

    states = session.query(State).filter(State.name.contains("a")).all()
    for s in states:
        session.delete(s)

    session.commit()
