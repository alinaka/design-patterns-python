from pizza import Pizza
from stores import ChicagoPizzaStore, NYPizzaStore, PizzaStore


def main():
    ny_store: PizzaStore = NYPizzaStore()
    chicago_store: PizzaStore = ChicagoPizzaStore()

    pizza: Pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.get_name()}\n {pizza}\n")

    pizza: Pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza.get_name()}\n {pizza}\n")


if __name__ == "__main__":
    main()
