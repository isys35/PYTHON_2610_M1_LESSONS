"""
Напишите программу, в которой описывается функция,
предназначенная для создания объекта.
Объект создается на основе уже существующего объекта,
который передается функции в качестве аргумента.
В создаваемый объект добавляются только те неслужебные поля из исходного объекта,
которые имеют целочисленное значение.
"""


class TestClass:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)


def create_object(init_object):
    attrs = {key: value for key, value in init_object.__dict__.items() if isinstance(value, int)}
    return init_object.__class__(**attrs)


if __name__ == '__main__':
    test_object = TestClass(a=1, b="hello", c=3)
    result_object = create_object(test_object)
    print(result_object.a)
    print(result_object.c)
    print(result_object.b)
