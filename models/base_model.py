#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import sqalchemy
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel:
    """A base class for all common attributes/methods"""
    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime, default=(datetime.utcnow()), nullable=False)
    updated_at = Column(DateTime, default=(datetime.utcnow()), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates base model
        Args:
            args: won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if 'update_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                                        kwargs['updated_at'],
                                        '%Y-%m-%dT%H:%M:%S.%f'
                                        )
            else:
                kwargs['updated_at'] = datetime.now()

            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                                        kwargs['created_at'],
                                        '%Y-%m-%dT%H:%M:%S.%f'
                                        )
            else:
                kwargs['created_at'] = datetime.now()

            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())

            if '__class__' in kwargs:
                del kwargs['__class__']

            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if dictionary.get('_sa_instance_state'):
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """Delete the current instance from storage."""
        from models import storage
        storage.delete(self)
