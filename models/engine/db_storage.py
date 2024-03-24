#!/usr/bin/python3
"""This module defines a db_storge class"""
from os import getenv
from models.base_model import Base
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.user import User

__model_classes = {"State": State, "Amenity": Amenity,
             "City": City, "Place": Place,
             "Review": Review, "User": User}


class DBStorage:
    """DBStorage class"""
    __eng = None
    __sess = None

    def __init__(self):
        """init """
        self.__eng = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__eng)

    def all(self, cls=None):
        """get all cls object from mysql"""
        my_dict = {}
        if cls is None:
            for cl in __model_classes.values():
                objs = self.__sess.query(cl).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    my_dict[key] = obj
        else:
            objs = self.__sess.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                my_dict[key] = obj
        return my_dict
    

    def new(self, obj):
        """add the object to the current database"""
        self.__sess.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__sess.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        self.__sess.delete(obj)

    def reload(self):
        """relod from db"""
        Base.metadata.create_all(self.__eng)
        Session = sessionmaker(bind=self.__eng, expire_on_commit=False)
        self.__sess = Session()
