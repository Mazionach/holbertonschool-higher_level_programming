#!/usr/bin/python3

"""
Script to list states from database
using SQLAlchemy
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}")

    Base.metadata.create_all(engine)
    sescla = sessionmaker(bind=engine)

    session = sescla()

    for s in session.query(State).order_by(State.id):
        print(f"{s.id}: {s.name}")

    session.close()
