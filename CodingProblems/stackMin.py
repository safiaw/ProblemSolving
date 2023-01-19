
class stackArray:

    def __init__(self,size):

        self.size=size
        self.array=[]*size
        self.top=-1
        self.minval=10000
        self.minarray=[]

    def push(self,elem):

        if self.isFull():
            print("Stack overflow")
        else:
            if self.minval > elem:
               self.minval=elem
               self.minarray.append(self.minval)
            
            self.top+=1
            self.array.append(elem)
            print("Pushed element is %d" %elem)
            self.showstack()

    def pop(self):

        if self.isEmpty():
            print("Stack underflow")
        else:
            
            value=self.array[self.top]
            self.array.remove(self.array[self.top])
            self.top-=1
            print("Poped element is %d" %value)
            if value in self.minarray:
                self.minarray.remove(value)
                #print(self.minarray)
                #self.minval=self.minarray[-1]
                
            self.showstack()

    def min(self):
        if self.isEmpty():
            print("Stack underflow")
        else:
            if self.minarray[-1]:
                self.minval=self.minarray[-1]
                print("Minimum value in stack is %d" %self.minval)
            else:
                print("Stack is empty and hence no minimum value")

    def showstack(self):
        print("Stack contents are:", self.array)
            
    def isFull(self):

        if self.top==(self.size-1):
            return True
        return False

    def isEmpty(self):

        if self.top==-1:
            return True
        return False


stack = stackArray(5)
stack.push(4)
stack.push(3)
stack.push(9)
stack.push(6)
stack.push(1)
stack.push(12)

stack.min()

stack.pop()
stack.min()

stack.pop()
stack.min()

stack.pop()
stack.min()

stack.pop()
stack.min()

stack.pop()
stack.min()
