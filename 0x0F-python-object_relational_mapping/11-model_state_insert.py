#!/usr/bin/python3
""" Script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    username, password, database = argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State()
    new_state.name = "Louisiana"
    session.add(new_state)
    state = session.query(State).filter_by(name="Louisiana").first()
    print(state.id)
    session.commit()


if __name__ == '__main__':
    main()
