#!/usr/bin/python3
"""This module instantiates a storage object.

   If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   it instantiates a database storage engine (DBStorage).
   Otherwise, it instantiates a file storage engine (FileStorage).
"""

from os import getenv


if getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
