import time


class ToyClass:
    def instancemethod(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


class Dog:
    barking = "Гав"
    whining = "Ууууу"

    def __init__(self, name: str):
        self.playing_time = 10
        self.name = name
        self.master = None

    def bark(self):
        print(self.barking)

    def whine(self):
        print(self.whining)

    def set_master(self, name: str):
        self.master = name

    def play_with_master(self):
        if not self.master:
            self.whine()
        else:
            print(f"{self.name} играет с {self.master}")
            self.bark()
            time.sleep(self.playing_time)



def main():
    dog = Dog("Шарик")
    dog_2 = Dog("Полкан")
    dog_2.barking = "Ауф"
    dog.set_master("Инокентий")
    dog.play_with_master()
    dog_2.bark()


if __name__ == '__main__':
    main()
    # toy = ToyClass()
    # print(toy.instancemethod())
    # print(ToyClass.classmethod())
    # print(toy.staticmethod())
    # print(ToyClass.staticmethod())
