class Child:
    pass


class Human:
    pass


class OldMan:
    pass


def run(human):
    if isinstance(human, Child):
        print('Ребёнок бегает')
    elif isinstance(human, Human):
        print('Человек бегает')
    elif isinstance(human, OldMan):
        print("Старый человек не хочет бежать")


def pilosophy(human):
    if isinstance(human, Child):
        print('Ребёнок не хочет филосовствовать')
    elif isinstance(human, Human):
        print('Человек слишком занят для это')
    elif isinstance(human, OldMan):
        print("Выдаёт крутую мысль")


if __name__ == '__main__':
    child = Child()
    human = Human()
    old_man = OldMan()
    run(child)
    run(human)
    run(old_man)
    human.__class__ = OldMan
    run(human)


