from abc import ABC, abstractmethod

class FlyBehavior(ABC):

    @abstractmethod
    def fly() -> None:
        pass
    

class QuackBehavior:

    @abstractmethod
    def quack() -> None:
        pass