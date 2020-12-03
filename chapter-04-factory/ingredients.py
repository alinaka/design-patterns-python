from typing import List


class Dough:
    pass


class ThinCrustDough(Dough):
    pass


class ThickCrustDough(Dough):
    pass


class Sauce:
    pass


class MarinaraSauce(Sauce):
    pass


class PlumTomatoSauce(Sauce):
    pass


class Cheese:
    pass


class ReggianoCheese(Cheese):
    pass


class Mozzarella(Cheese):
    pass


class Veggies:
    pass


class Garlic(Veggies):
    pass


class Onion(Veggies):
    pass


class Mushroom(Veggies):
    pass


class RedPepper(Veggies):
    pass


class BlackOlives(Veggies):
    pass


class Spinach(Veggies):
    pass


class EggPlant(Veggies):
    pass


class Pepperoni:
    pass


class SlicedPepperoni(Pepperoni):
    pass


class Clams:
    pass


class FreshClams(Clams):
    pass


class FrozenClams(Clams):
    pass


class PizzaIngredientFactory:
    def create_dough(self) -> Dough:
        raise NotImplementedError

    def create_sauce(self) -> Sauce:
        raise NotImplementedError

    def create_cheese(self) -> Cheese:
        raise NotImplementedError

    def create_veggies(self) -> List[Veggies]:
        raise NotImplementedError

    def create_pepperoni(self) -> Pepperoni:
        raise NotImplementedError

    def create_clam(self) -> Clams:
        raise NotImplementedError


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> List[Veggies]:
        veggies: List[Veggies] = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()

    def create_cheese(self) -> Cheese:
        return Mozzarella()

    def create_veggies(self) -> List[Veggies]:
        veggies: List[Veggies] = [BlackOlives(), Spinach(), EggPlant()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        return FrozenClams()
