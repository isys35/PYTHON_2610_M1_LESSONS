class User:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return str(f"00{self.__age}")

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError
        self.__age = age

    # age = property(get_age, set_age)

    # def get_age(self):
    #     return self.__age

    # def set_age(self, age):
    #     self.__age = age


if __name__ == '__main__':
    user = User("Олег", 22)
    print(user.age)
    user.age = 25
    print(user.age)
