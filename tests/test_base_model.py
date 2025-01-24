#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_creation(self):
        """Test creation of BaseModel instance."""
        instance = BaseModel()
        self.assertTrue(isinstance(instance, BaseModel))
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))
    
    def test_to_dict(self):
        """Test the to_dict method."""
        instance = BaseModel()
        dict_rep = instance.to_dict()
        self.assertTrue(isinstance(dict_rep, dict))
        self.assertIn('__class__', dict_rep)
        self.assertEqual(dict_rep['__class__'], 'BaseModel')

if __name__ == "__main__":
    unittest.main()

