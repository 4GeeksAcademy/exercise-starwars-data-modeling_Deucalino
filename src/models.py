import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    email=Column(String(250), nullable=False)
    password=Column(String(250), nullable=False)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(250))
    homeworld = Column(String(250))
    url = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__='planet'
    planet_uid = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__='favorites'
    id=Column(Integer, primary_key=True)
    bestcharacter_uid=Column(Integer, ForeignKey('characters.uid'))
    bestplanet_uid=Column(Integer, ForeignKey('planet.planet_uid'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

