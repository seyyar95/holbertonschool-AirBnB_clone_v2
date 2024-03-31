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
