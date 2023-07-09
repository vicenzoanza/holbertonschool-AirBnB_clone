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
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        from models.base_model import BaseModel
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.user import User

        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    objects = json.load(file)
                    classes = {'BaseModel': BaseModel, 'User': User,
                               'State': State, 'City': City,
                               'Amenity': Amenity,
                               'Place': Place, 'Review': Review}

                    for key, value in objects.items():
                        clase = key.split('.')[0]
                        if clase in classes.keys():
                            self.__objects[key] = classes[clase](**value)

            except FileNotFoundError:
                pass
