
import stackInArray

class setOfStacks():

    def __init__(self,size):

        self.size=size
        self.sos={}
        self.stacknum=1

    def push(self,item):

        if len(self.sos)==0:

            newstack = stackInArray.stackArray(self.size)
            newstack.push(item)
            self.sos[self.stacknum]=newstack
            self.stacknum+=1
            #self.sos[self.stacknum].append(newstack.array)
            #self.sos[self.stacknum].append(newstack.top)
        else:
            laststack_key = list(self.sos.keys())[-1]
            laststack = self.sos[laststack_key]
            #laststack_top = self.sos[laststack_top][1]

            if not laststack.isFull():
                laststack.push(item)
            else:
                nstack = stackInArray.stackArray(self.size)
                nstack.push(item)
                self.sos[self.stacknum]=nstack
                self.stacknum+=1

        self.showsos()

    def pop(self):

        if len(self.sos)==0:
           print("Set of stacks are empty. Sorry no elements to remove\n\n")
        else:
          laststack_key = list(self.sos.keys())[-1]
          laststack  = self.sos[laststack_key]
          poppedelem=laststack.pop()
          if laststack.isEmpty():
              del self.sos[laststack_key]
          
        self.showsos()
    def popAt(self,index):
        
        specStack = self.sos[index]
        elem=specStack.pop()
        if specStack.isEmpty():
            del self.sos[index]
        self.showsos()
        return elem

    def showsos(self):
        
        for eachstack in self.sos:
            self.sos[eachstack].showstack()

sStacks = setOfStacks(3)
sStacks.push(4)
sStacks.push(7)
sStacks.push(1)
sStacks.push(9)
sStacks.push(10)
sStacks.push(2)
sStacks.push(8)
sStacks.push(5)

sStacks.pop()
sStacks.pop()
sStacks.pop()
sStacks.pop()
print(sStacks.popAt(1))









