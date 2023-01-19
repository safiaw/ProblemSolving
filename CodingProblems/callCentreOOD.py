
class CallHandler:

    # static or class variable for 3 levels of employees
    employee_levels = 3
    # static or final values of number of employees at each level
    num_respondents = 10
    num_managers = 3
    num_directors = 2

    # list of employees by level, list of respondents is in list on 0th row
    # list of managers is in list on 1st col
    # list of directors is in list on 2nd col 
    employee_levels_list = [[],[],[]]

    # queues for each calls rank
    callQueues = [[],[],[]]

    def __init__(self):
        pass
    
    # gets the first available employee who can handle this call
    def getHandlerForCall(self, call):
        pass

    def dispatchCall(self, call):

        emp = Employee()
        emp = getHandlerForCall(call)
        if emp!=None:
            emp.recieveCall(call)
            call.setHandler(emp)
        else:
            call.reply("Please wait for free employee to reply")
            # add the call to the queue of an employee with minimal rank
            callQueues.get(call.getRank().getValue()).add(call)
            
    # an employee got free. Look for the waiting call that the employee can server. Return True if we assigned a call, false otherwise
    def assignCall(self,emp):
        return True/False


class Call:

    _rank = Rank()
    _caller = Caller()
    _handler = Employee()

    def __init__(self, c):
        _rank = Rank.responder
        _caller = c

    def setHandler(self, emp):
        _handler = e

    def reply(self, message):
        pass
    def getRank(self):

        return _rank
    def setRank(self,r):
        _rank = r

    def incrementRank(self):
        pass
    def disconnect(self):
        pass


class Employee:

      def __init__(self, handler):
            _currentCall = Call()
            _currentCall = None
            _rank = Rank()

      # start the conversation
      def receiveCall(self,call):
          pass

      # the issue is resolved, finish the call
      def callCompleted(self):
          pass
      # if the issue is not resolved, escalate the call and assign a new call to the employee
      def escalateAndReassign(self):
          pass
      # assign an new call to an employee, if the employee is free
      def assignNewCall(self):
          pass
      # returns whether the employee is free or not
      def isFree(self):
          return True/False

      def getRank(self):
          return rank

class Director(Employee):
    def __init__(self):
        rank = Rank.Director
class Manager(Employee):
    def __init__(self):
        rank = Rank.Manager
class Respondent(Employee):
    def __init__(self):
        rank = Rank.Responder









        
