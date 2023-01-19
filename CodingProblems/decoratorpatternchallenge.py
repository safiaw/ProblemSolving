
import abc

class Pizzas(abc.ABC):


    def __init__(self,desc):

        self.desc = "Unknown pizza"

    def getDescription(self):
        return self.desc

    @abc.abstractmethod
    def cost(self):
        pass

class ThinCrustPizza(Pizzas):

    def __init__(self):
        self.desc="Thin Crust Pizza"

    def cost(self):
        return 4.5
    
class ThickCrustPizza(Pizzas):

    def __init__(self):
        self.desc="Thick Crust Pizza"

    def cost(self):
        return 3.5

class ToppingsDecorator(Pizzas):

    @abc.abstractmethod
    def getDescription(self):
        pass


class Cheese(ToppingsDecorator):

    def __init__(self,pizza):
        self.pizza=pizza

    def getDescription(self):
        return self.pizza.getDescription() + ",Cheese"


    def cost(self):
        return self.pizza.cost() + 1.5
    
class Olives(ToppingsDecorator):

    def __init__(self,pizza):
        self.pizza=pizza

    def getDescription(self):
        return self.pizza.getDescription() + ",Olives"


    def cost(self):
        return self.pizza.cost() + 1.0

class Peppers(ToppingsDecorator):

    def __init__(self,pizza):
        self.pizza=pizza

    def getDescription(self):
        return self.pizza.getDescription() + ",Peppers"


    def cost(self):
        return self.pizza.cost() + 0.65


pizza = ThinCrustPizza()
pizza = Cheese(pizza)
pizza = Cheese(pizza)
pizza = Olives(pizza)
pizza = Peppers(pizza)
print(pizza.getDescription() + "=$" + str(pizza.cost()))

        

    
