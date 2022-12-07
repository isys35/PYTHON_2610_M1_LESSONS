class Cat:

    def make_sound(self):
        print("Мяу!")


class Dog:

    def make_sound(self):
        print("Гав!")


tuple = (Cat(), Dog())

for animal in tuple:
    animal.make_sound()

