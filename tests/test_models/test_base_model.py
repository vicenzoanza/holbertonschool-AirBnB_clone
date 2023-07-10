#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from datetime import datetime


class test_BaseModel(unittest.TestCase):
    """test BaseModel class"""

    def test_creation(self):
        """checks if an instance is created"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_id_instance(self):
        """checks instance id"""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_updated_at(self):
        """checks updated_at"""
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_save(self):
        """checks save method"""
        bm = BaseModel()
        o_datetime = bm.updated_at
        bm.save()
        n_datetime = bm.updated_at
        self.assertNotEqual(o_datetime, n_datetime)

    def test_to_dict(self):
        """checks to_dict method"""
        bm = BaseModel()
        new_dict = bm.to_dict()
        self.assertIsInstance(new_dict, dict)
        self.assertIsInstance(new_dict["id"], str)
        self.assertIsInstance(new_dict["created_at"], str)
        self.assertIsInstance(new_dict["updated_at"], str)
    
    def test_str(self):
        """checks str method"""
        bm = BaseModel()
        string = f"[{bm.__class__.__name__}] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), string)

    if __name__ == "__main__":
            unittest.main()
