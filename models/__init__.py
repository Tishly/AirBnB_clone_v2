#!/usr/bin/python3
"""This module instantiates a storage object.

   If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   it instantiates a database storage engine (DBStorage).
   Otherwise, it instantiates a file storage engine (FileStorage).
"""

from os import getenv
from models.city import City
from models.review import Review
from models.place import Place
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


if getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
