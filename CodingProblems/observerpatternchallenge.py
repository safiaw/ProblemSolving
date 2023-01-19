
import abc
    
class WeatherStation(abc.ABC):

    @abc.abstractmethod
    def registerObserver(self, obs):   # add new observer to the list
        pass
    @abc.abstractmethod
    def removeObserver(self, obs):     # remove observer from the list
        pass
    @abc.abstractmethod
    def notifyObservers(self):         # notifies all observers in the list
                                       # if the data in the subject changes
        pass

class concreteWeatherStation(WeatherStation):        # must implements three mothods in the subject
    # interface and manages the list of observers and the data observers are interested in
    
    def __init__(self):
        self.observers=[]
        self.temp=None
        self.windspeed=None
        self.pressure=None
             
    def registerObserver(self,observer):
        # add observer to the list
        self.observers.append(observer)

    def removeObserver(self,observer):
        # remove observer from the list
        self.observers.remove(observer)
    def notifyObservers(self):
        # notify all observers in the list if there is change in data
        for each_obs in self.observers:
            each_obs.update(self.temp,self.windspeed,self.pressure)
            
    def setTemp(self,temp):
        self.temp=temp
        self.notifyObservers()
        
    def setWindspeed(self, winds):
        self.windspeed = winds
        self.notifyObservers()

    def setPressure(self,pressure):
        self.pressure = pressure
        self.notifyObservers()

class Observer(abc.ABC):  # can't instantiate abstract class with an asbtract method

    @abc.abstractmethod
    def update(self,value):
        pass

class UserInterface(Observer):

    def __init__(self, subject):
        self.subject = subject
        self.temp = None
        self.pressure=None
        self.windspeed=None
        self.subject.registerObserver(self)
    def update(self, temp,windspeed,pressure):
        self.temp=temp
        self.windspeed=windspeed
        self.pressure=pressure
        self.display()
    def display(self):
        print("Temperature is %s" %self.temp)
        print("Wind speed is %s" %self.windspeed)
        print("Pressure is %s" %self.pressure)

class Log(Observer):

    def __init__(self, subject):
        self.subject = subject
        self.temp = None
        self.pressure=None
        self.windspeed=None
        self.subject.registerObserver(self)
    def update(self, temp,windspeed,pressure):
        self.temp=temp
        self.windspeed=windspeed
        self.pressure=pressure
        self.log()
    def log(self):
        print("Temperature is %s" %self.temp)
        print("Wind speed is %s" %self.windspeed)
        print("Pressure is %s" %self.pressure)

class AlertSystem(Observer):

    def __init__(self, subject):
        self.subject = subject
        self.temp = None
        self.pressure=None
        self.windspeed=None
        self.subject.registerObserver(self)
    def update(self, temp,windspeed,pressure):
        self.temp=temp
        self.windspeed=windspeed
        self.pressure=pressure
        self.alert()
    def alert(self):
        print("Temperature is %s" %self.temp)
        print("Wind speed is %s" %self.windspeed)
        print("Pressure is %s" %self.pressure)

#concSubj = concreteSubject()
#subj = Subject()
#print(isinstance(concSubj,subj))
#print(issubclass(concreteSubject,Subject))
#print(isinterface(concreteSubject,Subject))

concSubj = concreteWeatherStation()
concObs = UserInterface(concSubj)
concObs1 = Log(concSubj)
concObs2 = AlertSystem(concSubj)
print(concSubj.observers)
concSubj.setTemp(44)
concSubj.setPressure(10)
concSubj.setWindspeed(120)
concSubj.setTemp(30)





    
