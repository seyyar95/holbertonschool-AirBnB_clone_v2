#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def setUp(self):
        """Set up test fixtures."""
        super().setUp()
        self.amenity = Amenity()

    def test_amenity_name_type(self):
        """Test the type of the name attribute."""
        self.amenity.name = "Amenity"
        self.assertIsInstance(self.amenity.name, str)
