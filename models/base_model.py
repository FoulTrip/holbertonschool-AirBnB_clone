#!/usr/bin/python3

"""
Class Model
"""

import uuid
from datetime import datetime
import json
import models


class BaseModel:
    """
    Define todos los atributos/métodos comunes para otras clases
    """

    def __init__(self, **kwargs):
        """
        Inicia la instancia de BaseModel
        """

        # Si se proporcionan argumentos con nombre, configurar los atributos correspondientes
        if kwargs != {}:
            for key, value in kwargs.items():
                # Si no se proporciona 'created_at', establecerlo como la hora actual
                if key == "created_at" or key == "updated_at":
                    # Convertir las cadenas de fecha y hora en objetos datetime
                    timeObj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, timeObj)
                    continue
                if key != "__class__":
                        setattr(self, key, value)

            # Si no se proporciona 'updated_at', establecerlo como la hora actual
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

            # Si no se proporciona 'created_at', establecerlo como la hora actual
            if "created_at" not in kwargs:
                self.created_at = datetime.now()

            # Si no se proporciona 'id', generar un UUID y convertirlo a string
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())

        else:
            # Si no se proporcionan argumentos, generar un UUID y convertirlo a string
            self.id = str(uuid.uuid4())

            # Establecer 'created_at' como la hora actual
            self.created_at = datetime.now()

            # Establecer 'updated_at' como la hora actual
            self.updated_at = datetime.now()
            
            models.storage.new(self)

    def __str__(self):
        """
        Imprimo la instancia de BaseModel
        """
        return "[{:s}] ({:s}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Actualiza el atributo publico 'updated_at' con la fecha y hora actuales
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Devuelve un diccionario que contiene todas las claves y valores de __dict__ de la instancia
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__

        # Convertir 'created_at' y 'updated_at' a formato ISO y agregarlos al diccionario
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict

    @classmethod
    def from_dict(cls, data_dict):
        """
        Crea una nueva instancia de BaseModel a partir de un diccionario
        """

        return cls(**data_dict)

    @classmethod
    def from_json_string(cls, json_string):
        """
        Recreates an instance from a JSON string representation
        """
        obj_dict = json.loads(json_string)
        return cls(**obj_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of instances to a file as a JSON string
        """
        filename = cls.__name__ + ".json"
        obj_list = [obj.to_dict() for obj in list_objs]
        with open(filename, "w") as f:
            json.dump(obj_list, f)

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file and returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                obj_list = json.load(f)
                return [cls.from_dict(obj) for obj in obj_list]
        except FileNotFoundError:
            return []
