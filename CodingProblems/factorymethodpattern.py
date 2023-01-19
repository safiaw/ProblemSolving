import abc

class PizzaStore(abc.ABC):

    @abc.abstractmethod
    def createPizza(self,pizzatype):
        pass
    
    def orderPizza(self, pizzatype):
        pizza = Pizza()
        pizza = self.createPizza(pizzatype)
        print("Making a " + pizza.getName())
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

class ChicagoStylePizzaStore(PizzaStore):

    def createPizza(self, pizzatype):

        if pizzatype=="cheese":
            return ChicagoStyleCheesePizza()
        elif pizzatype=="veggie":
            return ChicagoStyleVeggiePizza()
        elif pizzatype=="clam":
            return ChicagoStyleClamPizza()
        elif pizzatype=="Pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            return None
        
class NYStylePizzaStore(PizzaStore):

    def createPizza(self, pizzatype):

        if pizzatype=="cheese":
            return NYStyleCheesePizza()
        elif pizzatype=="veggie":
            return NYStyleVeggiePizza()
        elif pizzatype=="clam":
            return NYStyleClamPizza()
        elif pizzatype=="Pepperoni":
            return NYStylePepperoniPizza()
        else:
            return None

class Pizza:

    def __init__(self):
        self.name='None'
    def getName(self):
        return self.name
    def prepare(self):
        pass
    def bake(self):
        pass
    def cut(self):
        pass
    def box(self):
        pass
    
class NYStyleCheesePizza(Pizza):

    def __init__(self):
        self.name='NY style cheese pizza'
    def prepare(self):
        pass
    def bake(self):
        pass

class NYStyleVeggiePizza(Pizza):

    def __init__(self):
        pass
    def prepare(self):
        pass
    def bake(self):
        pass
class NYStyleClamPizza(Pizza):

    def __init__(self):
        pass
    def prepare(self):
        pass
    def bake(self):
        pass
class NYStylePepperoniPizza(Pizza):

    def __init__(self):
        pass
    def prepare(self):
        pass
    def bake(self):
        pass


class ChicagoStyleClamPizza(Pizza):

    def __init__(self):
        pass
    def prepare(self):
        pass
    def bake(self):
        pass

class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        pass
    def prepare(self):
        pass
    def bake(self):
        pass

class ChicagoStyleVeggiePizza(Pizza):

    def __init__(self):
        self.name='Chicago style veggie pizza'
    def prepare(self):
        pass
    def bake(self):
        pass

class ChicagoStylePepperoniPizza(Pizza):

    def __init__(self):
        self.name='pepperoni'
  
    def prepare(self):
        pass
    def bake(self):
        pass

pizza = Pizza()
nystore = NYStylePizzaStore()
pizza = nystore.orderPizza("cheese")
print("Safia ordered a " + pizza.getName() + "\n")

pizza = Pizza()
chicagostore = ChicagoStylePizzaStore()
pizza = chicagostore.orderPizza("veggie")
print("Safia ordered a " + pizza.getName() + "\n")

    
        





    
        




    
        



