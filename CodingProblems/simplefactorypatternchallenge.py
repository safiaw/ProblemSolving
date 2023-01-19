import abc

class Calendar(abc.ABC):

   def __init__(self,timezone):
      self.zone = None
    
   def print(self):
       print("This is a " + self.zone.getDisplayName())
       print("Its offset is " + self.zone.getOffset())
       
   @abc.abstractmethod
   def createCalendar(self):
       pass

class pacificCalendar(Calendar):

    def __init__(self):
        self.timezone='pacific'
        self.zone = ZoneFactory().createZone(self.timezone)

    def createCalendar(self):
        print("Creating a pacific time zone calendar")

class ZoneFactory:

    def __init__(self):
        self.zone=Zone()
    def createZone(self,zoneid):

        if zoneid=='central':
            self.zone=ZoneUSCentral()
        elif zoneid=='eastern':
            self.zone=ZoneUSEastern()
        elif zoneid=='mountain':
            self.zone=ZoneUSMountain()
        elif zoneid=='pacific':
            self.zone=ZoneUSPacific()
        return self.zone

class Zone:

    def __init__(self):
        self.displayName="None"
        self.offset="None"
    def getDisplayName(self):
        return self.displayName
    def getOffset(self):
        return self.offset

class ZoneUSCentral(Zone):

    def __init__(self):
        self.displayName="US Central TimeZone"
        self.offset="- 5 hrs GMT"

class ZoneUSEastern(Zone):

    def __init__(self):
        self.displayName="US Eastern TimeZone"
        self.offset="- 6 hrs GMT"

class ZoneUSMountain(Zone):

    def __init__(self):
        self.displayName="US Mountain TimeZone"
        self.offset="- 7 hrs GMT"

class ZoneUSPacific(Zone):

    def __init__(self):
        self.displayName="US Pacific TimeZone"
        self.offset="- 8 hrs GMT"

cal = pacificCalendar()
#print(cal.zone)
cal.print()


    
        





    
        




    
        



