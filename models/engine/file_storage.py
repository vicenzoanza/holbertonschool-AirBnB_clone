#!/usr/bin/python3#
""" FIleStorage """

import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        # Obtenemos el nombre de la calse "obj" y luego el id
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    objects = json.load(file)
                    self.__objects = {}
                    for key, value in objects.items():
                        self.__objects[key] = BaseModel(**value)

            except FileNotFoundError:
                pass
