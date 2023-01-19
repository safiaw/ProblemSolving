#!/usr/bin/python3

# We'll use python Lists which is similar to Java ArrayList for implementing stack. 
# This stack can grow on runtime and it's size is not fixed

class stackArray:

    def __init__(self,size):
     
        self.size=size
        self.array = []*size      
        self.top = -1

    def push(self, elem):

        if self.isFull():
           print("Stack overflow")
        else:
           
           self.array.append(elem)
           self.top+=1
           #print("Pushed element is %d" %elem)
           #self.showstack()


    def pop(self):

        if self.isEmpty():
           print("Stack underflow")

        else:
           value = self.array[self.top]  
           #print(value)
           self.array.remove(value)
           self.top-=1
           #print("Popped element is %d" %value)
           return value
           #self.showstack()        

    def peek(self):
        
        if self.isEmpty():
           print("Stack is Empty")
        else:
           value=self.array[self.top]
           print("top value of stack is %d" %value)
           #return value

    def isEmpty(self):

        if self.top==-1:
           print("stack is empty")
           return True
        return False
    

    def isFull(self):
        
        if self.top==(self.size-1):
           print("stack is full")
           return True
        return False

    def showstack(self):
       
        print("Stack:", self.array)

'''
stack = stackArray(5)
stack.push(2)
stack.push(3)
stack.pop()
stack.peek()
stack.pop()
stack.peek()
'''
