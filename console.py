#!/usr/bin/python3
"""Firts Console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Exit")
        return True

    def do_create(self, arg):
        """new instance of BaseModel, saves it (to the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        class_arg = arg.split()
        class_name = class_arg[0]
        if class_name not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            key = class_name + "." + args[1]
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            key = class_name + "." + args[1]
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name."""
        args = arg.split()
        obj_dict = storage.all()

        if not args:
            new_list = []
            for key, value in obj_dict.items():
                new_list.append(str(value))
            print(new_list)
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            new_list = []
            for key, value in obj_dict.items():
                if key.startswith(args[0] + "."):
                    new_list.append(str(value))
            print(new_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file)"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key not in all_objs:
                print("** no instance found **")
            else:
                instance = all_objs[key]
                if instance.__class__.__name__ in HBNBCommand.class_list:
                    setattr(instance, args[2], args[3])
                    instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
