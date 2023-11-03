import unittest
import json
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """
    Clase para realizar pruebas unitarias a la clase User.
    """

    def setUp(self):
        """
        Método que se ejecuta antes de cada prueba. Crea una instancia de User.
        """
        self.user = User()

    def test_init(self):
        """
        Prueba el método __init__ para asegurar que la instancia se crea correctamente.
        """
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_to_dict(self):
        """
        Prueba el método to_dict para asegurar que devuelve un diccionario correcto.
        """
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["id"], self.user.id)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

    def test_from_dict(self):
        """
        Prueba el método from_dict para asegurar que crea una instancia correcta a partir de un diccionario.
        """
        user_dict = self.user.to_dict()
        new_user = User.from_dict(user_dict)
        self.assertEqual(new_user.id, self.user.id)
        self.assertEqual(new_user.created_at, self.user.created_at)
        self.assertEqual(new_user.updated_at, self.user.updated_at)

    def test_from_json_string(self):
        """
        Prueba el método from_json_string para asegurar que crea una instancia correcta a partir de una cadena JSON.
        """
        user_json = json.dumps(self.user.to_dict())
        new_user = User.from_json_string(user_json)
        self.assertEqual(new_user.id, self.user.id)
        self.assertEqual(new_user.created_at, self.user.created_at)
        self.assertEqual(new_user.updated_at, self.user.updated_at)

    def test_save_to_file_and_load_from_file(self):
        """
        Prueba los métodos save_to_file y load_from_file para asegurar que guardan y cargan correctamente las instancias en un archivo.
        """

        users = [self.user]

        # Guarda la lista de instancias en un archivo como una cadena JSON
        User.save_to_file(users)

        # Carga las instancias desde un archivo JSON y devuelve una lista de instancias
        loaded_users = User.load_from_file()

        # Busca la instancia guardada en la lista de instancias cargadas
        for user in loaded_users:
            if user.id == self.user.id:
                loaded_user = user
                break
        else:
            assert False, "User not found in loaded users"

        # Comprueba que la instancia cargada es igual a la instancia guardada
        # 'updated_at' será diferente porque 'save_to_file' lo actualiza
        self.assertEqual(loaded_user.id, self.user.id)
        self.assertEqual(loaded_user.created_at, self.user.created_at)


if __name__ == "__main__":
    unittest.main()
