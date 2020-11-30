from abc import ABC, abstractmethod


class Beverage(ABC):
    description: str = "Unknown description"

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass


class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return .89


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast"

    def cost(self) -> float:
        return .99


class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf"

    def cost(self) -> float:
        return 1.05


class Mocha(CondimentDecorator):
    beverage: Beverage

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return .20 + self.beverage.cost()


class Soy(CondimentDecorator):
    beverage: Beverage

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Soy"

    def cost(self) -> float:
        return .15 + self.beverage.cost()


class Whip(CondimentDecorator):
    beverage: Beverage

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return .10 + self.beverage.cost()


def main():
    beverage: Beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost()}")

    beverage2: Beverage = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()} ${beverage2.cost()}")

    beverage3: Beverage = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()} ${beverage3.cost()}")


if __name__ == "__main__":
    main()
