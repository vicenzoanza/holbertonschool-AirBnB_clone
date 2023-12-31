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
        if not args:
            print("** class name missing **")
        else:
            class_name = args.split()
            if class_name[0] not in self.classes:
                print("** class doesn't exist **")
                return
            elif len(class_name) < 2:
                print("** instance id missing **")
                return

            o_key = class_name[0] + '.' + class_name[1]
            if o_key not in storage.all():
                print("** no instance found **")
            else:
                del (storage.all()[o_key])
                storage.save()

    def do_all(self, args):
        """ """
        class_name = args.split()

        if len(args) == 0:
            objects = storage.all()
            obj = [str(value) for value in objects.values()]
            print(obj)
            return

        elif class_name[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            objects = storage.all()
            obj = [str(v) for k, v in objects.items() if class_name[0] in k]
            print(obj)

    def do_update(self, args):
        """ """
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args.split()
        if class_name[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(class_name) < 2:
            print("** instance id missing **")
            return
        elif len(class_name) < 3:
            print("** attribute name missing **")
            return
        elif len(class_name) < 4:
            print("** value missing **")
            return

        o_key = class_name[0] + "." + class_name[1]
        if o_key not in storage.all():
            print("** no instance found **")
            return
        else:
            instance = storage.all()[o_key]
            if class_name[3][0] == '"' and class_name[3][-1] == '"':
                setattr(instance, class_name[2], class_name[3][1:-1])
            else:
                setattr(instance, class_name[2], class_name[3])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
