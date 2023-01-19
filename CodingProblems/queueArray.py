
class myQueue:

    def __init__(self,size):

        self.size=size
        self.array=[]*size
        self.rear=-1
        self.front=-1

    def insert(self,elem):

         if self.isEmpty():
             self.array.append(elem)
             self.rear+=1
             self.front+=1
             #print("Pushed element is %d" %elem)
         
         elif self.isFull():
              print("Queue is full!")
              return

         elif self.front<=self.rear:
               self.array.append(elem)
               self.rear+=1
               #print("Pushed element is %d" %elem)
         
         
         #self.showqueue() 

    def remove(self):

         if self.isEmpty():
            print("Queue is empty")
            return
         
         else:

           if self.front==self.rear:            
                 value=self.array[self.front]
                 self.array.remove(value)
                 self.front=-1
                 self.rear=-1
                 #print("Removed element is %d" %value)

           elif self.front < self.rear:
                 value = self.array[self.front]
                 self.array.remove(value)
                 self.front=0
                 self.rear-=1
                 #print("Removed element is %d" %value)
         
         return value
         #self.showqueue()


    def peek(self):
        
         if self.isEmpty():
             print("Queue is empty")
         else:
             val=self.array[self.front]
             print("Top of the queue is %d" %val)

    def isEmpty(self):

        if self.front==-1 and self.rear==-1:
            return True
        return False


    def isFull(self):

        if self.rear==self.size-1:
           return True
        return False


    def showqueue(self):

        print("Queue contents are:", self.array)


queue = myQueue(5)
queue.insert(2)
queue.insert(3)
queue.insert(4)
queue.remove()
queue.remove()
queue.peek()
queue.remove()
queue.insert(5)
queue.peek()


