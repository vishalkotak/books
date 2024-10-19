
from behavior_interfaces import FlyBehavior, QuackBehavior

class FlyWithWings(FlyBehavior):

    def fly(self) -> None:
        print(f"I am flying.")


class FlyNoWay(FlyBehavior):
    
    def fly(self) -> None:
        print(f"I can't fly")


class FlyWithRockets(FlyBehavior):

    def fly(self) -> None:
        print(f"I am duck with flying rocket.")


class Quack(QuackBehavior):

    def quack(self) -> None:
        print(f"Quack")


class MuteQuack(QuackBehavior):
    
    def quack(self) -> None:
        print(f"Silence")


class Squeak(QuackBehavior):

    def quack(self) -> None:
        print(f"Squeak")