#!/usr/bin/python3
"""
<<<<<<< HEAD
Module for the User class.
=======
Defines the User class.
>>>>>>> 24103b9f0f67f6e0446e8bbc4fe21666dfd27f0b
"""
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """
    class User that handles users' information
=======
    """Represent a User

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name

>>>>>>> 24103b9f0f67f6e0446e8bbc4fe21666dfd27f0b
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
