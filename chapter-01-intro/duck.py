from abc import ABC

from fly_behaviors import FlyBehavior, FlyNoWay, FlyWithWings
from quack_behaviors import QuackBehavior, Quack


class Duck(ABC):
    fly_behavior: FlyBehavior = None
    quack_behavior: QuackBehavior = None

    def display(self) -> None:
        pass

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb: FlyBehavior) -> None:
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior) -> None:
        self.quack_behavior = qb

    def swim(self) -> None:
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self) -> None:
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior: FlyBehavior = FlyNoWay()
        self.quack_behavior: QuackBehavior = Quack()

    def display(self) -> None:
        print("I'm a model duck!")
