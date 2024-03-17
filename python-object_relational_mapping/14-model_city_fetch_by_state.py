#!/usr/bin/python3

"""
Script to list cities from database
using SQLAlchemy
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}")

    sescla = sessionmaker(bind=engine)

    session = sescla()

    states = session.query(State).order_by(State.id)

    for c in session.query(City).order_by(City.id):
        print(f"{states[c.state_id]}: ({c.id}) {c.name}")

    session.close()
