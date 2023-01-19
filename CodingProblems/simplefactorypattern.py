'''
class PizzaStore:

    def __init__(self,pizzatype):
        self.type=pizzatype
    
    def orderPizza(self):

        if self.type == "cheese":
            pizza = CheesePizza()
        elif self.type == "veggie":
            pizza = VeggiePizza()
        elif self.type == "greek":
            pizza = GreekPizza()
        elif self.type == "pepperoni":
            pizza = PepperoniPizza()
        
        pizza.prepare()
        pizza.cook()
        return pizza '''

''' In a growing pizza restaurent, a number of new pizza types keeps on adding.
Adding the new pizza type every time in the above code will make the code open
for change, violating the Open-Closed principle. Therefore, we can separate the
code that varies and encapsulate it'''

class SimplePizzaFactory:

    def __init__(self,pizzatype):
        self.type=pizzatype
        self.pizza = Pizza()
    def createPizza(self):
        if self.type == "cheese":
            self.pizza = CheesePizza()
        elif self.type == "veggie":
            self.pizza = VeggiePizza()
        elif self.type == "greek":
            self.pizza = GreekPizza()
        elif self.type == "pepperoni":
            self.pizza = PepperoniPizza()
        return self.pizza

class PizzaStore:

    def __init__(self):
        self.pizza = Pizza()
         
    def orderPizza(self,pizzatype):
        self.pizza = SimplePizzaFactory(pizzatype).createPizza()
        print("Got an order of a " +self.pizza.getDescription())
        self.pizza.prepare()
        self.pizza.bake()
        #return self.pizza

class Pizza:

    def __init__(self):
        self.description='None'

    def getDescription(self):
        return self.description
        
    def prepare(self):
        pass
    def bake(self):
        pass
    def cut(self):
        pass
    def box(self):
        pass
    
class CheesePizza(Pizza):

    def __init__(self):
        self.description='cheese pizza'
    def prepare(self):
        print("Preparing a cheese pizza")
    def bake(self):
        pass

class VeggiePizza(Pizza):

    def __init__(self):
        pass
    def prepare(self):
        pass
    def bake(self):
        pass


class ClamPizza(Pizza):

    def __init__(self):
        pass
    def prepare(self):
        pass
    def bake(self):
        pass

class PepperoniPizza(Pizza):

    def __init__(self):
        pass
    def prepare(self):
        pass
    def bake(self):
        pass

pizzastore = PizzaStore()
pizzastore.orderPizza('cheese')

    
        





    
        




    
        



