#!/usr/bin/python3

"""
    Module contain FileStorage class
"""

import json


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
        new_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def save(self):
        """
        Serializa __objects al archivo JSON
        """

        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Deserializa el archivo JSON a __objects (solo si el archivo JSON existe; de lo contrario, no hace nada).
        Si el archivo no existe, no debe generar ninguna excepción.
        """
        
        with open(self.__file_path, "r") as f:
            temp_dict = json.load(f)
        for key, value in temp_dict.items():
                class_name = value["__class__"]
                obj = eval(class_name)(**value)
                self.__objects[key] = obj
