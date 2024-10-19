from abc import ABC, abstractmethod
from behavior import FlyWithWings, Quack, FlyWithRockets
from behavior_interfaces import FlyBehavior, QuackBehavior

class Duck:

    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None

    @abstractmethod
    def display(self) -> None:
        pass

    def fly_helper(self):
        self.fly_behavior.fly()

    def quack_helper(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb: FlyBehavior) -> None:
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior) -> None:
        self.quack_behavior = qb


class MallardDuck(Duck):

    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print(f"I am a Mallard duck.")


class RocketDuck(Duck):

    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print(f"I am a rocket duck.")


def main():
    mallard_duck = MallardDuck()
    mallard_duck.fly_helper()
    mallard_duck.quack_helper()
    mallard_duck.display()

    rocket_duck = RocketDuck()
    rocket_duck.fly_helper()
    rocket_duck.quack_helper()
    rocket_duck.display()

    # Dynamically set fly behavior
    rocket_duck.set_fly_behavior(FlyWithRockets())
    rocket_duck.fly_helper()

if __name__ == "__main__":
    main()
        