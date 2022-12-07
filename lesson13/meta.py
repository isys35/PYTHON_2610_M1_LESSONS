from lesson9.example3.decorators import brenchmark


class C:

    def __init__(self, c):
        print(c)


def make_class(class_name):
    class C:
        def print_class_name(self):
            print(class_name)

    return C


def my_custom_init(self, name, age):
    self.name = name
    self.age = age


def my_metaclass(name, parent, attrs):
    return "Hello"


class ClassWithMeta(metaclass=my_metaclass):
    pass


def brenchmark_meta(name, parent, attrs):
    my_attrs = {}
    for attr_name, attr_value in attrs.items():
        my_attrs[attr_name] = attr_value
        if hasattr(attr_value, '__call__'):
            my_attrs[attr_name] = brenchmark(attr_value)
    return type(name, parent, my_attrs)


def only_private_attrs(name, parent, attrs):
    for attr_name in attrs:
        if not attr_name.startswith(f'_{name}__') and not attr_name.startswith('__'):
            raise ValueError
    return type(name, parent, attrs)


class OnlyPrivateClass(metaclass=only_private_attrs):
    __default_name = "<und>"


class BrenchClass(metaclass=brenchmark_meta):

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


class meta(type):

    def __new__(cls, *args, **kwargs):
        attrs = args[2]
        for attr_name in attrs:
            if not attr_name.startswith(f'_{args[0]}__') and not attr_name.startswith('__'):
                raise ValueError
        new_args = (args[0], args[1], attrs)
        return super().__new__(cls, *new_args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("__call__")
        print(self, args, kwargs)
        return super().__call__(*args, **kwargs)

    def __setattr__(self, key, value):
        raise ValueError


class D(metaclass=meta):
    __default_name = "dsds"



if __name__ == '__main__':
    # C1, C2 = map(make_class, ["C1", "C2"])
    # c1 = C1()
    # c2 = C2()
    # c1.print_class_name()
    # c2.print_class_name()
    # NewClass = type('NewClas', (object,), {"attribute": 12})
    # print(NewClass)
    # obj = NewClass()
    # print(obj.attribute)
    # ClassWithInit = type('ClassWithInit', (object,), {"__init__": my_custom_init})
    # print(ClassWithInit)
    # obj_with_init = ClassWithInit("Виктор", 18)
    # print(obj_with_init.name)
    # print(obj_with_init.age)
    # print(type(ClassWithMeta))
    # obj = BrenchClass("Игорь")
    # obj.print_name()
    d = D()
    D.abc = 15
    print(D.abc)
