from duck import Duck, MallardDuck, ModelDuck
from fly_behaviors import FlyRocketPowered


def main():
    mallard: Duck = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model: Duck = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()


if __name__ == "__main__":
    main()
