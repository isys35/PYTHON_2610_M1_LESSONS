class Person:
    default_name = "<undefined>"
    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    def __init__(self, name: str):
        self.name = name

    # def __init_subclass__(cls, **kwargs):
    #     cls.default_name = "SUPERADMIN"

    def __del__(self):
        print(f"{self} Удалён")

    def __repr__(self):
        return f'Персонаж: {self.name}'

    def __str__(self):
        return self.name

    def __int__(self):
        return 42

    def __call__(self, *args, **kwargs):
        print(args)

    def __bool__(self):
        if self.name.startswith("А"):
            return True
        return False

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False



if __name__ == '__main__':
    # person = Person("Игорь")
    # person_2 = Person("Витя")
    # print(person.name, person_2.name)
    person = Person("Антон")
    # person_2 = Person("Дмитрий")
    # print(person == person_2)
    # print(person.name)
    # print(getattr(person, "name"))
    # setattr(person, "profession", "плотник")
    # print(person.profession)
    # print(dir(person))
    # print(person.__sizeof__())
    # print(person)
    # print(int(person))
    # if person:
    #     print("Истина")
    # person()
    viktor = person.__class__('Витю')
    print(viktor)
    print(viktor.__dict__)