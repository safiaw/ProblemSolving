
class stackArray:

    def __init__(self,size):

        self.size=size
        self.array=[]*size
        self.top=-1

    def push(self,elem):

        if self.isFull():
            print("Stack overflow")
        else:
            self.top+=1
            self.array.append(elem)
            print("Pushed element is %d" %elem)
            #self.showstack()

    def pop(self):

        if self.isEmpty():
            print("Stack underflow")
        else:
            value=self.array[self.top]
            self.array.remove(self.array[self.top])
            self.top-=1
            print("Poped element is %d" %value)
            return value
            #self.showstack()

    def peek(self):
        if self.isEmpty():
            print("Stack underflow")
        else:
            print(self.array[self.top])
            return self.array[self.top]

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

'''
stack = stackArray(5)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.pop()
stack.peek()'''

