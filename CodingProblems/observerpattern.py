
import abc
    
class Subject(abc.ABC):

    #obs = Observer()
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

class concreteSubject(Subject):        # must implements three mothods in the subject
    # interface and manages the list of observers and the data observers are interested in
    #observer = Observer()
    def __init__(self):
        self.observers=[]
        self.value=0
             
    def registerObserver(self,observer):
        # add observer to the list
        self.observers.append(observer)

    def removeObserver(self,observer):
        # remove observer from the list
        self.observers.remove(observer)
    def notifyObservers(self):
        # notify all observers in the list if there is change in data
        for each_obs in self.observers:
            each_obs.update(self.value)
    def setValue(self,value):
        self.value=value
        self.notifyObservers()

class Observer(abc.ABC):  # can't instantiate abstract class with an asbtract method

    @abc.abstractmethod
    def update(self,value):
        pass

class concreteObserver(Observer):

    #subject = concreteSubject()
    def __init__(self, subject):
        self.subject = subject
        self.value=0
        self.subject.registerObserver(self)
    def update(self, value):
        self.value=value
        self.display()
    def display(self):
        print("Value is %d" %self.value)

#concSubj = concreteSubject()
#subj = Subject()
#print(isinstance(concSubj,subj))
#print(issubclass(concreteSubject,Subject))
#print(isinterface(concreteSubject,Subject))

concSubj = concreteSubject()
concObs = concreteObserver(concSubj)
concObs1 = concreteObserver(concSubj)
concObs2 = concreteObserver(concSubj)
print(concSubj.observers)
concSubj.setValue(11)





    
