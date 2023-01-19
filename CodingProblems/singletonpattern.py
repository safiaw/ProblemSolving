
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """
    
class SingletonMeta(type):

    _instances={}

    # __init__ - a magic method used to initialise newly created object
    def  __call__(cls,*args,**kwargs):   #another magic method used to make the
        # instance of a class callable, implements a function call operator
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """

        if cls not in cls._instances:
            instance = super().__call__(*args,**kwargs)
            cls._instances[cls]=instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        pass

'''
class Restaurant:

    _instance=None

    @staticmethod
    def static():
        if Restaurant._instance==None:
            Restaurant._instance = Restaurant()
        return Restaurant._instance
'''
r1=Singleton()
r2=Singleton()
if id(r1)==id(r2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, both variables contain different instances.")
