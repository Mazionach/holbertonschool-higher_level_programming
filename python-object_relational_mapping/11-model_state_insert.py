#!/usr/bin/python3

"""
Script to add a state to database
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

    n = State(name="Louisiana")
    session.add(n)
    session.commit()

    print(f"{n.id}")
