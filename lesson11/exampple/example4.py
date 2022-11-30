
class Person:
    type = "Person"
    description = "Some Description"
    default_name = "<undefined>"

    def __init__(self, name=None):
        self.name = name if name else Person.default_name



    def print_type(self):
        print(self.type)


print(Person.type)
print(Person.description)

Person.description = "New Description"

print(Person.description)

dima = Person("Дима")
oleg = Person("Олег")
print(dima.type)
print(oleg.type)

dima.type = "Class Person"
dima.print_type()
oleg.print_type()


Person.type = "Super puper type"

dima.print_type()
oleg.print_type()