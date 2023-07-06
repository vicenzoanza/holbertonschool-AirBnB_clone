#!/usr/bin/python3#
""" FIleStorage """

import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
            return self.__objects

    def new(self, obj):
        # Obtenemos el nombre de la calse "obj" y luego el id
            key = f"{obj.__class__.__name__}{obj.id}"
            self.__objects[key] = obj
    
    def save(self):
            with open(self.__file_path, 'w') as file:
                json.dump(self.__objects, file)

    def reload(self):
            if os.path.exists(self.__file_path):
                with open(self.__file_path, 'r') as file:
                    self.__objects = json.load(file)
