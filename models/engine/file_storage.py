#!/usr/bin/python3

"""
    Module contain FileStorage class
"""

import json
from datetime import datetime
from models import storage


class FileStorage:
    """
    Class FileStorage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Devuelve el diccionario __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Establece en __objects el objeto con la clave <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Actualiza el atributo publico 'updated_at' con la fecha y hora actuales
        """
        self.update_at = datetime.now()
        storage.new(self)
        storage.save()

    def reload(self):
        """
        Deserializa el archivo JSON a __objects (solo si el archivo JSON existe; de lo contrario, no hace nada).
        Si el archivo no existe, no debe generar ninguna excepción.
        """

        try:
            with open(FileStorage.__file_path, "r") as f:
                temp_dict = json.load(f)
            for key, value in temp_dict.items():
                class_name = value["__class__"]
                obj = eval(class_name)(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            print("Error deserializando")
