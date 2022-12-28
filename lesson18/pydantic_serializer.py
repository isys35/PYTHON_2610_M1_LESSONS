from pydantic import BaseModel, validator
import json


class User(BaseModel):
    name: str
    surname: str
    age: int

    @validator("age")
    def validate_age(cls, value):
        if int(value) < 20:
            raise ValueError("Слишком взрослый")
        return int(value)


with open("user.json", "r") as json_file:
    data_dict = json.load(json_file)

user = User(**data_dict)
print(user.name)
print(type(user.age))
print(user.__dict__)
