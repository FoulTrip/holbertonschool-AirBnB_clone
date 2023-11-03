#!/usr/bin/python3
"""
Consola para interactuar con el modelo
"""

import cmd
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
import models.base_model as s
import models


class HBNBCommand(cmd.Cmd):
    """
    Clase de la consola interactiva.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Salir de la consola.
        """
        return True

    def do_EOF(self, arg):
        """
        Manejar el final del archivo.
        """
        print()
        return True

    def do_create(self, arg):
        """
        Crea una nueva instancia de BaseModel, la guarda en el archivo JSON e imprime el id.
        """

        if not arg:
            print("** class name missing **")
            return
        try:
            if arg == "User":
                new_instance = User()
            elif arg == "BaseModel":
                new_instance = s.BaseModel()
            elif arg == "Amenity":
                new_instance == Amenity()
            elif arg == "City":
                new_instance = City()
            elif arg == "Place":
                new_instance = Place()
            elif arg == "Review":
                new_instance == Review()
            elif arg == "State":
                new_instance == State()

            new_instance.save()
            print(new_instance.id)
            models.storage.new(new_instance)
            models.storage.save()
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Imprime la representación de cadena de una instancia basada en el nombre de la clase y el id.
        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel" or "User":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = models.storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        obj_dict = models.storage.all()

        if not arg:
            print([str(obj_dict[key]) for key in obj_dict])
        elif not any(key.startswith(arg + ".") for key in obj_dict):
            print("** class doesn't exist **")
        else:
            print([str(obj_dict[key]) for key in obj_dict if key.startswith(arg + ".")])

    def do_destroy(self, arg):
        """
        Elimina una instancia basándose en el nombre de la clase y el id (guarda el cambio en el archivo JSON).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel" or "User":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = models.storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """
        Actualiza una instancia basándose en el nombre y el id de la clase añadiendo o actualizando un atributo.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            all_objs = models.storage.all()
            key = args[0] + "." + args[1]
            if key not in all_objs:
                print("** no instance found **")
            else:
                instance = all_objs[key]
                if isinstance(instance, s.BaseModel):
                    setattr(instance, args[2], args[3])
                    instance.save()

    def emptyline(self):
        """
        Evitar la ejecución del comando anterior si se presiona enter sin comando.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
