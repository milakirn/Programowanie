import os
import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

base_op = create_engine('sqlite:///match.db')
base = declarative_base()


class Team(base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teammates_id = Column(Integer, ForeignKey("teammates.id"))
    game_id = Column(Integer, ForeignKey("games.id"))


class Teammates(base):
    __tablename__ = "teammates"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    team = relationship('Team', 'teammates')


class Game(base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    team_1 = relationship('Team', 'games')
    team_2 = relationship('Team', 'games')
    score = Column(String, nullable=False)


base.metadata.create_all(base_op)

dbsession = sessionmaker(bind=base_op)
session = dbsession()

if not session.query(Team).count():
    session.add(Team(name="Los Angeles Lakers", teammate_id=1, game_id=1))
    session.add(Team(name="Chicago Bulls", teammate_id=2, game_id=2))
    session.add(Team(name="Washington Wizards", teammate_id=3, game_id=3))
    session.add(Team(name="Brooklyn Nets", teammate_id=4, game_id=4))
    session.add(Teammates(name="Jan1", suraname="Kowalski1"))
    session.add(Teammates(name="Jan2", suraname="Kowalski2"))
    session.add(Teammates(name="Jan3", suraname="Kowalski3"))
    session.add(Game(score="Coś"))
    session.add(Game(score="Bo"))
    session.add(Game(score="Nie"))
    session.add(Game(score="Znam"))

session.commit()
