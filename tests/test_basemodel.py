#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    class of unittest for the class model
    """

    def test_initializacion(self):
        """
        Firt test - initializacion of BaseModel
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.create_at)
        self.assertIsNotNone(my_model.updated_at)
        
    def test_str_method(self):
        """
        Prueba el método __str__ de BaseModel
        """
        my_model = BaseModel()
        string = "[{}] ({}) {}".format(my_model.__class__.__name__, my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), string)

    def test_save_method(self):
        """
        Prueba el método save de BaseModel
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """
        Prueba el método to_dict de BaseModel
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(my_model_dict['created_at']), str)
        self.assertEqual(type(my_model_dict['updated_at']), str)
        self.assertEqual(type(my_model_dict['id']), str)
