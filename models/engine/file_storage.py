#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            new_dict = {}
            for key, value in self.__objects.items():
                if value.__class__.__name__ == cls.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects
