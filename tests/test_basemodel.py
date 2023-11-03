import unittest
import json
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Clase para realizar pruebas unitarias a la clase BaseModel.
    """

    def setUp(self):
        """
        Método que se ejecuta antes de cada prueba. Crea una instancia de BaseModel.
        """
        self.model = BaseModel()

    def test_init(self):
        """
        Pruebo el método __init__ para asegurar que la instancia se crea correctamente.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        """
        Pruebo el método to_dict para asegurar que devuelve un diccionario correcto.
        """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_from_dict(self):
        """
        Pruebo el método from_dict para asegurar que crea una instancia correcta a partir de un diccionario.
        """
        model_dict = self.model.to_dict()
        new_model = BaseModel.from_dict(model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)

    def test_from_json_string(self):
        """
        Prueba el método from_json_string para asegurar que crea una instancia correcta a partir de una cadena JSON.
        """
        model_json = json.dumps(self.model.to_dict())
        new_model = BaseModel.from_json_string(model_json)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)

    def test_save_to_file_and_load_from_file(self):
        """
        Prueba los métodos save_to_file y load_from_file para asegurar que guardan y cargan correctamente las instancias en un archivo.
        """

        models = [self.model]

        # Guarda la lista de instancias en un archivo como una cadena JSON
        BaseModel.save_to_file(models)

        # Carga las instancias desde un archivo JSON y devuelve una lista de instancias
        loaded_models = BaseModel.load_from_file()

        # Busca la instancia guardada en la lista de instancias cargadas
        for model in loaded_models:
            if model.id == self.model.id:
                loaded_model = model
                break
        else:
            assert False, "Model not found in loaded models"

        # Comprueba que la instancia cargada es igual a la instancia guardada
        # 'updated_at' será diferente porque 'save_to_file' lo actualiza
        self.assertEqual(loaded_model.id, self.model.id)
        self.assertEqual(loaded_model.created_at, self.model.created_at)


if __name__ == "__main__":
    unittest.main()
