from abc import abstractmethod, ABC
from typing import Optional

from ingredients import ChicagoPizzaIngredientFactory, NYPizzaIngredientFactory
from pizza import CheesePizza, ClamPizza, PepperoniPizza, Pizza, VeggiePizza


class PizzaStore(ABC):
    def order_pizza(self, kind):
        pizza: Pizza = self.create_pizza(kind)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, type: str) -> Optional[Pizza]:
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, item: str) -> Optional[Pizza]:
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()
        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("NY Style Sauce and Cheese Pizza")
        elif item == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("NY Style Pepperoni Pizza")
        elif item == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("NY Style Clam Pizza")
        elif item == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("NY Style Veggie Pizza")
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, item: str) -> Optional[Pizza]:
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()
        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Sauce and Cheese Pizza")
        elif item == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("Chicago Style Pepperoni Pizza")
        elif item == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Clam Pizza")
        elif item == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("Chicago Style Veggie Pizza")
        return pizza
