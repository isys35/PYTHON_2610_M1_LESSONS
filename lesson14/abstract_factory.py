from abc import ABC, abstractmethod


class MeleeWeapon(ABC):

    @abstractmethod
    def show_melee_weapon(self):
        pass


class RangedWeapon(ABC):

    @abstractmethod
    def show_ranged_weapon(self):
        pass


class Sword(MeleeWeapon):

    def show_melee_weapon(self):
        print("Двуручный меч")


class Katana(MeleeWeapon):

    def show_melee_weapon(self):
        print("Катана")


class Bow(RangedWeapon):

    def show_ranged_weapon(self):
        print("Лук")


class TeppoUmi(RangedWeapon):

    def show_ranged_weapon(self):
        print("Тэппо Юми")


class AbstractFabric(ABC):

    @abstractmethod
    def get_melee_weapon(self) -> MeleeWeapon:
        pass

    @abstractmethod
    def get_ranged_weapon(self) -> RangedWeapon:
        pass


class GermanFabric(AbstractFabric):

    def get_melee_weapon(self) -> MeleeWeapon:
        return Sword()

    def get_ranged_weapon(self) -> RangedWeapon:
        return Bow()


class JapanFabric(AbstractFabric):


    def get_melee_weapon(self) -> MeleeWeapon:
        return Katana()

    def get_ranged_weapon(self) -> RangedWeapon:
        return TeppoUmi()


if __name__ == '__main__':
    country = int(input("Выберите страну: 1 - Япония, 2 - Германия "))
    weapon = int(input("Выберите тип оружия: 1 - Оружие ближнего боя, 2 - Оружие дальнего боя "))
    country_classes = {1: JapanFabric, 2: GermanFabric}
    weapon_methods = {1: "get_melee_weapon", 2: "get_ranged_weapon"}
    print(country_classes[country]().__getattribute__(weapon_methods[weapon])())

