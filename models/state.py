#!/usr/bin/python3
""" a class State that inherits from BaseModel"""

"""
Defines the State class
"""

from models.base_model import BaseModel


class State(BaseModel):

    """Represent a state

    Attributes:
        name (str): The name of the state

    """

    name = ""
