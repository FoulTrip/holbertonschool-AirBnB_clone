#!/usr/bin/python3

"""
Class Model
"""

import uuid
from datetime import datetime
import json

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()


class BaseModel:
    """
    Define todos los atributos/métodos comunes para otras clases
    """

    def __init__(self, *args, **kwargs):
        """
        Inicia la instancia de BaseModel
        """

        # Si se proporcionan argumentos con nombre, configurar los atributos correspondientes
        if kwargs:
            for key, value in kwargs.items():
                # Evito agregar el atributo '__class__' al objeto
                if key != "__class__":
                    # Si no se proporciona 'created_at', establecerlo como la hora actual
                    if key == "created_at" or key == "updated_at":
                        # Convertir las cadenas de fecha y hora en objetos datetime
                        setattr(
                            self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        )
                    else:
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

    def __str__(self):
        """
        Imprimo la instancia de BaseModel
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Actualiza el atributo publico 'updated_at' con la fecha y hora actuales
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Devuelve un diccionario que contiene todas las claves y valores de __dict__ de la instancia
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__

        # Convertir 'created_at' y 'updated_at' a formato ISO y agregarlos al diccionario
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
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
                return [cls.from_json_string(json.dumps(obj)) for obj in obj_list]
        except FileNotFoundError:
            return []


# test 01

# # if __name__ == "__main__":
#     # Prueba básica
#     my_model = BaseModel()
#     my_model.name = "My First Model"
#     my_model.my_number = 89
#     print(my_model)
#     my_model.save()
#     print(my_model.to_dict())

# # test 02

# if __name__ == "__main__":
#     my_model = BaseModel()
#     my_model.name = "My First Model"
#     my_model.my_number = 89
#     print(my_model)
#     my_model.save()
#     print(my_model)
#     my_model_json = my_model.to_dict()
#     print(my_model_json)
#     print("JSON de my_model:")
#     for key, value in my_model_json.items():
#         print(f"\t{key}: ({type(value)}) - {value}")

#     new_model = BaseModel.from_dict(my_model_json)
#     print("\nRecreated Model:")
#     print(new_model)

# test 03

# if __name__ == "__main__":
#     # Crear una instancia de BaseModel y probar su funcionalidad
#     my_model = BaseModel()
#     my_model.name = "My First Model"
#     my_model.my_number = 89
#     my_model.save()
#     print(my_model)

#     # Crear una segunda instancia de BaseModel y probar su funcionalidad
#     my_model2 = BaseModel()
#     my_model2.name = "My Second Model"
#     my_model2.my_number = 42
#     my_model2.save()
#     print(my_model2)

#     # Imprimir todos los objetos almacenados en el almacenamiento de archivos
#     all_objs = my_model2.storage.all()
#     print("-- All objects --")
#     for obj_id in all_objs.keys():
#         obj = all_objs[obj_id]
#         print(obj)
