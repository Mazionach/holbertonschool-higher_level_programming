#!/usr/bin/python3

"""
Script to print first state from database
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

    if (s := session.query(State).order_by(State.id).first()) is not None:
        print(f"{s.id}: {s.name}")
    else:
        print("Nothing")

    session.close()
