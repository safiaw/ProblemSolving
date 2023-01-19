
# a client class

class DuckSimulator:

    def __init__(self):

        duck = Duck()
        # instantiating a subclass
        mduck = MallardDuck()
        # test a duck
        self.testDuck(mduck)

        # test a turkey
        drone = SuperDrone()
        droneadapter = DroneAdapter(drone)
        self.testDuck(droneadapter)

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
class Drone(abc.ABC):

    @abc.abstractmethod
    def beep(self):
        pass
    @abc.abstractmethod
    def spin_rotors(self):
        pass
    @abc.abstractmethod
    def take_off(self):
        pass
    
# a class that implements the adaptee interface
class SuperDrone(Drone):
     
     def beep(self):
         print("Beep beep beep")
     def spin_rotors(self):
         print("Rotors are spinning")
     def take_off(self):
         print("Taking off")

# an adapter implements the target interface and redirect/delegates its behavior
# calls to the adaptee interface class behavior

class DroneAdapter(Duck):

    def __init__(self, drone):
        self.drone = drone
    def quack(self):
        self.drone.beep()
    def fly(self):
        self.drone.take_off()
        for i in range(0,5):
            self.drone.spin_rotors()

dsimul = DuckSimulator()




        
         

    
