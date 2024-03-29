#!/usr/bin/python3
"""
    tests for FileStorage
"""
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from sqlalchemy.engine.base import Engine
import logging


class test_DBStorage(unittest.TestCase):
    """
        Base test class
    """
    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        try:
            cls.dummy = DBStorage()
        except Exception as e:
            logging.error(f"Error setting up DBStorage instance: {e}")
            cls.dummy = None

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy


if __name__ == "__main__":
    unittest.main()
