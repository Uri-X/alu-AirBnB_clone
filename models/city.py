#!/usr/bin/python3
""" a class User that inherits from BaseModel"""
"""This module creates a city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""
    state_id = ""
    name = ""
