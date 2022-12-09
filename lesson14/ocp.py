from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):

    def make_sound(self):
        print("roar")


class Mouse(Animal):

    def make_sound(self):
        print("squek")


class Cat(Animal):

    def make_sound(self):
        print("meow")


animals = [
    Lion('lion'),
    Mouse('mouse'),
    Cat("cat")
]


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)
