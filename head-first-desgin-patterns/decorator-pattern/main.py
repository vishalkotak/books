from abc import ABC, abstractmethod

# Not a fan of this approach as it causes nesting which is hard to keep track of.

class Beverage(ABC):

    def __init__(self):
        self.description = ""

    def get_description(self) -> str:
        return self.description        

    @abstractmethod
    def cost(self) -> float:
        pass


class HouseBlend(Beverage):

    def __init__(self):
        self.description = "House Blend"

    def cost(self) -> float:
        return 1.0
    

class DarkRoast(Beverage):

    def __init__(self):
        self.description = "Dark Roast"

    def cost(self) -> float:
        return 1.0
    

class Espresso(Beverage):

    def __init__(self):
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.0
    

class Decaf(Beverage):

    def __init__(self):
        self.description = "Decaf"

    def cost(self) -> float:
        return 1.0


class CondimentDecorator:

    def __init__(self):
        self.beverage = None
    
    def get_description(self) -> str:
        pass

    
class Milk(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + "Milk"
    
    def cost(self) -> float:
        return self.beverage.cost() + 2.0
    

class Soy(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + "Soy"
    
    def cost(self) -> float:
        return self.beverage.cost() + 2.0
    

class Sugar(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + "Sugar"
    
    def cost(self) -> float:
        return self.beverage.cost() + 2.0
    

def main():
    espresso = Espresso()
    print(f"{espresso.get_description() + " - " + str(espresso.cost())}")

    beverage = DarkRoast()
    beverage = Milk(beverage=beverage)
    beverage = Sugar(beverage=beverage)
    print(f"{beverage.get_description() + " - " + str(beverage.cost())}")


if __name__ == "__main__":
    main()