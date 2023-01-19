
import abc

class Beverage(abc.ABC):


    def __init__(self,desc):

        self.desc = "Unknown beverage"

    def getDescription(self):
        return self.desc

    @abc.abstractmethod
    def cost(self):
        pass

class DarkRoast(Beverage):

    def __init__(self):
        self.desc="Dark Roast Coffee"

    def cost(self):
        return .99
    
class HouseBlend(Beverage):

    def __init__(self):
        self.desc="House Blend coffee"

    def cost(self):
        return 1.2

class CondimentDecorator(Beverage):

    @abc.abstractmethod
    def getDescription(self):
        pass


class Whip(CondimentDecorator):

    def __init__(self,beverage):
        self.beverage=beverage

    def getDescription(self):
        return self.beverage.getDescription() + ",Whip"


    def cost(self):
        return self.beverage.cost() + .10
    
class Mocha(CondimentDecorator):

    def __init__(self,beverage):
        self.beverage=beverage

    def getDescription(self):
        return self.beverage.getDescription() + ",Mocha"


    def cost(self):
        return self.beverage.cost() + .30


beverage = DarkRoast()
beverage = Whip(beverage)
beverage = Whip(beverage)
beverage = Mocha(beverage)
print(beverage.getDescription() + "=$" + str(beverage.cost()))

        

    
