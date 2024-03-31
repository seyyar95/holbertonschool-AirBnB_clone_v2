#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    id = Column(
            String(60),
            nullable=False,
            primary_key=True
            )
    created_at = Column(
            DateTime,
            nullable=False,
            default=datetime.utcnow()
            )
    updated_at = Column(
            DateTime,
            nullable=False,
            default=datetime.utcnow()
            )

    
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """
        Initializer for the BaseModel class.
        """

        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tformat)
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value
