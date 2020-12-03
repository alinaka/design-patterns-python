from abc import ABC, abstractmethod
from typing import List

from ingredients import Cheese, Clams, Dough, Pepperoni, PizzaIngredientFactory, Sauce, Veggies


class Pizza(ABC):
    name: str
    dough: Dough
    sauce: Sauce
    cheese: Cheese
    pepperoni: Pepperoni
    veggies: List[Veggies]
    clam: Clams

    @abstractmethod
    def prepare(self) -> None:
        raise NotImplementedError

    def bake(self) -> None:
        print("Bake for 25 minutes at 350")

    def cut(self) -> None:
        print("Cutting pizza into diagonal slices")

    def box(self) -> None:
        print("Place pizza in official PizzaStore box")

    def get_name(self) -> str:
        return self.name

    def set_name(self, name) -> None:
        self.name = name

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


class CheesePizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()

    def __str__(self) -> str:
        ingredients = map(lambda x: x.__class__.__name__,
                          [self.dough, self.sauce, self.cheese])
        return f"{list(ingredients)}"


class ClamPizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()

    def __str__(self) -> str:
        ingredients = map(lambda x: x.__class__.__name__,
                          [self.dough, self.sauce, self.cheese, self.clam])
        return f"{list(ingredients)}"


class PepperoniPizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()

    def __str__(self) -> str:
        ingredients = map(lambda x: x.__class__.__name__,
                          [self.dough, self.sauce, self.cheese, self.pepperoni])
        return f"{list(ingredients)}"


class VeggiePizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.veggies = self.ingredient_factory.create_veggies()

    def __str__(self) -> str:
        ingredients = map(lambda x: x.__class__.__name__,
                          [self.dough, self.sauce, self.veggies])
        return f"{list(ingredients)}"
