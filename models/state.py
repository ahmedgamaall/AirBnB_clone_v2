#!/usr/bin/python3
""" State Module for HBNB project """
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """This State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='delete', backref='state')
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
	    from models.city import City
            from models import storage
            cts_lst = []
            for ct in storage.all(City).values():
                if ct.state_id == self.id:
                    cts_lst.append(ct)
            return cts_lst
