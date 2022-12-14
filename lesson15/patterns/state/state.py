from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def philosophy(self):
        pass


class ChildState(State):

    def run(self):
        print("Ребёнок бегает")

    def philosophy(self):
        print("Ребёнок не хочет филосовствовать")


class HumanState(State):

    def run(self):
        print("Человек бегает")

    def philosophy(self):
        print("Человек слишком занят для этого")


class OldManState(State):

    def run(self):
        print("Старый человек не хочет бежать")

    def philosophy(self):
        print("Выдаёт крутую мысль")


class PeopleContext:

    def __init__(self, state):
        self.change_state(state)

    def change_state(self, state):
        self._state = state

    def run(self):
        self._state.run()

    def pilosophy(self):
        self._state.philosophy()


if __name__ == '__main__':
    context = PeopleContext(OldManState())
    context.run()
    context.change_state(HumanState())
    context.run()