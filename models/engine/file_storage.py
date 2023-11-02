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

    @classmethod
    def all(cls):
        """
        Devuelve el diccionario __objects
        """

        return cls.__objects

    def new(self, obj):
        """
        Establece en __objects el objeto con la clave <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializa __objects al archivo JSON
        """

        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializa el archivo JSON a __objects (solo si el archivo JSON existe; de lo contrario, no hace nada).
        Si el archivo no existe, no debe generar ninguna excepción.
        """

        try:
            with open(self.__file_path, "r") as f:
                temp_dict = json.load(f)
            for key, value in temp_dict.items():
                class_name = value["__class__"]
                if class_name == "BaseModel":
                    from models.base_model import BaseModel
                    obj = BaseModel(**value)
                elif class_name == "User":
                    from models.user import User
                    obj = User(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            print("El archivo no existe, imposible cargar datos")
        except Exception as ex:
            print(f"Error durante la carga: {ex}")
