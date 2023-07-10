#!/usr/bin/python3
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_file_storage(unittest.TestCase):
    """Class that contains all test for FileStorage"""

    def test_file_path(self):
        """Checks __file_path attribute"""
        fs = FileStorage()
        self.assertEqual(fs._FileStorage__file_path, 'file.json')

    def test_objects(self):
        """checks __objects attribute"""
        fs = FileStorage()
        self.assertIsInstance(fs._FileStorage__objects, dict)

    def test_all(self):
        """Checks if all returns a dictonary"""
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

    def test_new(self):
        """checks new method"""
        fs = FileStorage()
        add_base = BaseModel()
        fs.new(add_base)
        self.assertNotEqual(fs._FileStorage__objects, {})

    def test_save(self):
        """checks save method"""
        fs = FileStorage()
        all_dict = fs.all()
        add_base = BaseModel()
        fs.save()
        self.assertNotEqual(all_dict, {})

    def test_reload(self):
        """checks reload"""
        fs = FileStorage()
        fs.all().clear()
        fs.reload()
        self.assertNotEqual(len(fs.all()), 0)

if __name__ == "__main__":
    unittest.main()
