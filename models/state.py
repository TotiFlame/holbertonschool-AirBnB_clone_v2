#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: name of MySQL table
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """
            It returns a list of City objects that
                are associated with the current State object
            :return: A list of City objects
            """
            from models import storage
            from models.city import City
            # return list of City objs in __objects
            c_dict = storage.all(City)
            c_list = []

            # copy values from dict to list
            for city in c_dict.values():
                if city.state_id == self.id:
                    c_list.append(city)

            return c_list
