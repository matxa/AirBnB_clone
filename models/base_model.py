#!/usr/bin/python3
""" BaseModel class which all other classes inhirit from """
from datetime import datetime
import models
import uuid


class BaseModel():
    """Base Model"""

    def __init__(self, *args, **kwargs):
        """Init
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at":
                    kwargs[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k == "updated_at":
                    kwargs[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string
        repr
        """
        print_tuple = (self.__class__.__name__, self.id, self.__dict__)
        s = "[{}] ({}) {}".format(*print_tuple)
        return s

    def save(self):
        """save the updated
        time of last modification
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary containing
        all keys
        """
        copy_dict = self.__dict__.copy()
        copy_dict['created_at'] = self.created_at.isoformat()
        copy_dict['updated_at'] = self.updated_at.isoformat()
        copy_dict['__class__'] = self.__class__.__name__
        return copy_dict
