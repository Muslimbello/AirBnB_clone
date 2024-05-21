import uuid
from datetime import datetime
import json
from os import path


class BaseModel:
    """BaseModel class"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    """returns string representaion of the Basemodel"""

    def __str__(self):
        return f"{self.__class__.__name__} {self.id} {self.__dict__}"

    """ returns dictionary representation of the BaseModel"""

    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    """updates the public instance updated_at"""

    def save(self):
        self.updated_at = datetime.now()


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
