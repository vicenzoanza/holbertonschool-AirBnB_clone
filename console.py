#!/usr/bin/python3
""" console """

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity

classes = ["BaseModel", "User", "Place", "State", "Review", "City", "Amenity"]


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """ """
        return True

    def do_EOF(self, args):
        """ """
        exit(0)

    def emptyline(self):
        """ """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
