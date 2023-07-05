#!/usr/bin/python3
""" Airbnb Clone """


import uuid
from datetime import datetime


class BaseModel:
    """ Creating BaseModel class """
    def __init__(self, *args, **kwargs):
        if kwargs != "":
            if '__class__' in kwargs:
                del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        # Primero convertimos un id unico y lo convertimos en string
        self.id = str(uuid.uuid4())
        # Le pasamos el horario actual al crear una instancia
        self.created_at = datetime.now()
        # Le pasamos a update_at el horario de created_at
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        return{
                **self.__dict__,
                '__class__': self.__class__.__name__,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()
            }
