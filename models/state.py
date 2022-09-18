#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City",  backref="state", cascade="all, delete")

    else:
        @property
        def cities(self):
            """Returns a list of City instances with
            `state_id` equals to the current `State.id`
            """
            c_list = []
            for c_instance in list(models.storage.all(City).values()):
                if c_instance.state_id == State.id:
                    c_list.append(c_instance.state_id)
            return c_list
