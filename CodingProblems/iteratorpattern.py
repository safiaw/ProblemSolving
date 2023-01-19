
import abc

class Menu(abc.ABC):

    @abc.abstractmethod
    def createIterator(self):
        pass

class DinerMenu(Menu):

    def createIterator(self):

        return DinerMenuIterator(menuItems)

class PancakeHouseMenu(Menu):

    def createIterator(self):

        return PancakeHouseIterator()

class Iterator(abc.ABC):

    @abc.abstractmethod
    def hasNext(self):
        pass
    @abc.abstractmethod
    def next(self):
        pass

class PancakeHouseIterator(Iterator):

    def __init__(self,listItems):
        self.position=0
        self.list=listItems
        
    def hasNext(self):
        # increment position
        # return the next item


    def next(self):
        # is there another item in the array?
        # returns True or False


class DinerMenuIterator(Iterator):

    def __init__(self,listItems):
        self.position=0
        self.list=listItems
        
    def hasNext(self):
        # increment position
        # return the next item


    def next(self):
        # is there another item in the array?
        # returns True or False


class Cafe:

    def __init__(self,pancakeHouseMenu, dinerMenu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu

    def printMenu(self, iterator):
        while iterator.hasNext():
            menuItem = iterator.next()
            # print the menu
        
        
