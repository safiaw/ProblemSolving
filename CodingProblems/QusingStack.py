import stackInArray

class Qstacks():

    def __init__(self,size):
 
        self.size=size
        self.stack1 = stackInArray.stackArray(size)
        self.stack2 = stackInArray.stackArray(size)

    def insert(self,item):

        if not self.stack1.isFull():
            self.stack1.push(item)
            self.stack1.showstack()
        else:
            print("Queue is full!!\n")

    def remove(self):

        if not self.stack1.isEmpty():

            while not self.stack1.isEmpty():
                 
                elem=self.stack1.pop()
                self.stack2.push(elem)

            poppedelem = self.stack2.pop()

            while not self.stack2.isEmpty():

                elem = self.stack2.pop()
                self.stack1.push(elem)
                
            self.stack1.showstack()
        else:

            print("Queue is empty!!!\n")


qstack = Qstacks(5)
qstack.insert(8)
qstack.insert(1)
qstack.insert(9)
qstack.insert(10)
qstack.insert(2)
qstack.insert(11)
qstack.insert(12)

qstack.remove()
qstack.remove()
