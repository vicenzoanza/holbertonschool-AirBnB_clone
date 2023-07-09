#!/usr/bin/python3
""" Airbnb Clone """


import uuid
from datetime import datetime
import models


class BaseModel:
    """ Creating BaseModel class """
    def __init__(self, *args, **kwargs):

        date = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, date)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, date)
                if key == 'id':
                    self.id = str(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ prints str """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dict containing all keys/values of __dict__ """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
