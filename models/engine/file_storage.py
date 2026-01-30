#!/usr/bin/python3
"""
FileStorage module - serializes instances to JSON file
and deserializes JSON file to instances
"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "State": State,
        "City": City
    }

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <class name>.id"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if file exists)"""
        if not os.path.isfile(FileStorage.__file_path):
            return

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)

            FileStorage.__objects.clear()  # clear old objects
            for key, value in obj_dict.items():
                class_name = value.get("__class__")
                if class_name in FileStorage.__classes:
                    cls = FileStorage.__classes[class_name]
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance
        except Exception:
            pass  # silent fail if file is corrupted
