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


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place",
               "State", "Review", "City", "Amenity"]

    def do_quit(self, args):
        """ """
        return True

    def do_EOF(self, args):
        """ """
        exit(0)

    def emptyline(self):
        """ """
        pass

    def do_create(self, args):
        """ """
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args.strip()
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        class_objs = globals()[class_name]
        instance = class_objs()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """ """
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args.split()) < 2:
            print("** instance id missing **")
            return

        class_n2 = args.split()[0]
        key = f"{class_n2}.{args.split()[1]}"
        ins = storage.all()

        if key not in ins:
            print("** no instance found **")
            return

        instance = ins[key]
        print(instance)

    def do_destroy(self, args):
        """ """
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        idd = args.split()[0]
        ins = models.storage.get(self.classes[class_name], idd)
        if ins:
            ins.delete()
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ """
        class_name = None

        if len(args) == 0:
            objects = storage.all()
            obj = [str(value) for value in objects.values()]
            print(obj)
        else:
            class_name = args.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        obj = [str(value) for key, val in objects.items() if class_name in key]
        print(obj)

    def do_update(self, args):
        """ """
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args.strip()
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        elif len(args.split()) < 2:
            print("** instance id missing **")
            return

        idd = args.split()[1]
        ins = models.storage.get(self.classes[class_name], idd)
        if ins:
            ins.delete()
            models.storage.save()
        else:
            print("** no instance found **")

        if len(args.split()) < 3:
            print("** attribute name missing **")
            return

        if len(args.split()) < 4:
            print("** value missing **")
            return

        setattr(objs[key], args.split()[2], eval(args.split()[3]))
        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
