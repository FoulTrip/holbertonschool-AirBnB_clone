#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        className = self.__class__.__name__
        return f"[{className}] ({self.id}) ({self.__dict__})"

    def to_dict(self):
        dictCopy = self.__dict__.copy()
        dictCopy["__class__"] = self.__class__.__name__
        dictCopy["created_at"] = self.created_at.isoformat()
        dictCopy["updated_at"] = self.updated_at.isoformat()
        return dictCopy
