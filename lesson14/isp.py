from abc import ABC, abstractmethod


class IShape(ABC):

    @abstractmethod
    def draw(self):
        pass



class Square(IShape):

    def draw(self):
        print("Квадрат")



if __name__ == '__main__':
    square = Square()