#!/usr/bin/python3
"""
Consola para interactuar con el modelo
"""

import cmd
from models.base_model import BaseModel
from models import storage


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
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Imprime la representación de cadena de una instancia basada en el nombre de la clase y el id.
        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        all_objs = storage.all()
        if len(arg) == 0:
            print([str(all_objs[key]) for key in all_objs])
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            print(
                [str(all_objs[key]) for key in all_objs if key.startswith("BaseModel")]
            )

    def do_destroy(self, arg):
        """
        Elimina una instancia basándose en el nombre de la clase y el id (guarda el cambio en el archivo JSON).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """
        Actualiza una instancia basándose en el nombre y el id de la clase añadiendo o actualizando un atributo.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
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
                setattr(instance, args[2], args[3])
                instance.save()

    def emptyline(self):
        """
        Evitar la ejecución del comando anterior si se presiona enter sin comando.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
