from abc import ABC, abstractmethod


class Hero(ABC):

    @abstractmethod
    def attack(self):
        pass


class Archer(Hero):

    def attack(self):
        print("Стрельба из лука")


class C(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

    @classmethod
    @abstractmethod
    def class_abstract_method(cls):
        pass

    @staticmethod
    @abstractmethod
    def static_abstract_method():
        pass

    @property
    @abstractmethod
    def abstract_property(self):
        pass

    @abstract_property.setter
    @abstractmethod
    def abstract_property(self, value):
        pass



if __name__ == '__main__':
    archer = Archer()
    archer.attack()