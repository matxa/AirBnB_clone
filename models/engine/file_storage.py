#!/usr/bin/python3
""" FileStorage class which serializes/deserializes JSON file to instances """
import json
import os.path
from os import path
from models.base_model import BaseModel


class FileStorage():
    """ FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all key, v"""
        return FileStorage.__objects

    def new(self, obj):
        """new obj"""
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """save to file"""
        new_dict = {}
        for k, v in FileStorage.__objects.items():
            new_dict.update({k: v.to_dict()})
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """getting from file"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                file_content = json.loads(file.read())
            for k, v in file_content.items():
                obj_to_reload = eval(v['__class__'])(**v)
                FileStorage.__objects.update({k: obj_to_reload})
