
# a client class

class DuckSimulator:

    def __init__(self):
         
        # instantiating a subclass
        mduck = MallardDuck()
        # test a duck
        self.testDuck(mduck)

        # test a turkey
        turkey = WildTurkey()
        turkeyadapter = TurkeyAdapter(turkey)
        self.testDuck(turkeyadapter)

    def testDuck(self,duck):
        duck.quack()
        duck.fly()


import abc

# a target interface to which the adapter converts an adaptee interface into 
class Duck(abc.ABC):

    def quack(self):
        pass
    def fly(self):
        pass
    
# a class that implements the target interface
class MallardDuck(Duck):

    def quack(self):
        print("MallardDuck quack quack quack")

    def fly(self):
        print("Mallard Duck is flying")

# an adaptee interface with different behavior than the target interface
class Turkey(abc.ABC):

    @abc.abstractmethod
    def gobble(self):
        pass
    @abc.abstractmethod
    def fly(self):
        pass
    
# a class that implements the adaptee interface
class WildTurkey(Turkey):
     
     def gobble(self):
         print("Turkey gobble gobble gobble")
     def fly(self):
         print("Turkey is flying")

# an adapter implements the target interface and redirect/delegates its behavior
# calls to the adaptee interface class behavior

class TurkeyAdapter(Duck):

    def __init__(self, turkey):
        self.turkey = turkey
    def quack(self):
        self.turkey.gobble()
    def fly(self):
        for i in range(0,5):
            self.turkey.fly()

dsimul = DuckSimulator()




        
         

    
