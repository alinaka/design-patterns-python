class FlyBehavior:
    def fly(self) -> None:
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying!")


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly!")


class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying with a rocket!")
