from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


tom = Person("Tom", 38)
tom2 = Person("Tom", 38)
print(tom == tom2)
print(f"Name: {tom.name}  Age: {tom.age}")
