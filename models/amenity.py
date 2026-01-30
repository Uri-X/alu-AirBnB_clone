#!/usr/bin/python3
""" a class Amenity that inherits from BaseModel"""
"""
This is a Module for Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Custom amenity class

    Attributes:
        name(str): amenity name

    """
    name = ""
