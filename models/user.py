#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
import sqalchemy

class User(BaseModel, Base):
    """This class defines a user
    Attributes:
        email: user's email address
        password: user's password
        first_name: user's first name
        last_name: user's last name
        """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
            backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
            backref="user")
