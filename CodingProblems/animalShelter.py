
class Node():

    def __init__(self,value=None):
        self.data=value
        self.next=None


class AnimalShelter():

    def __init__(self):
        self.head=Node()

    def adopt(self,adoptType):
        if adoptType=='Dog':
            self.__dequeueDog()
        elif adoptType=='Cat':
            self.__dequeueCat()
        else:
            self.__dequeueAny()

    def enqueue(self,data):
        # add node at the end of the list
        end=Node(data)
        n=self.head
        while n.next!=None:
              n=n.next
        n.next=end

    def __dequeueAny(self):

        if self.head.next==None:
           print("\nSorry, we don't have any animals for adoption!!\n")
        else:
           animal = self.head.next.data
           self.head.next = self.head.next.next
           #self.head.next=None
           print("\nAdopting an oldest animal!!\n")
           print(animal)
           sll.printll()

    def __dequeueDog(self):
        
        n=self.head.next
        if n==None:
            print("No animals for adoption!!")
            return
        elif 'd' in n.data:
            adoptDog=n.data
            self.head.next=self.head.next.next
        else:            
           while n.next!=None:
              if 'd' in n.next.data:
                   adoptDog=n.next.data
                   n.next=n.next.next
                   break
              n=n.next
        if n.next==None and 'd' not in n.data:
            print("\nSorry, we don't have dogs available for adoption!!\n")
        else:
            print("\nAdopting an oldest Dog!!\n")
            print(adoptDog)
            self.printll()
                
    def __dequeueCat(self):

        n=self.head.next
        if n==None:
            print("No animals for adoption!!")
            return
        elif 'c' in n.data:
            adoptCat=n.data
            self.head.next=self.head.next.next
        else:
           while n.next!=None:
              if 'c' in n.next.data:
                   adoptCat=n.next.data
                   n.next=n.next.next
                   break
              n=n.next
        if n.next==None and 'c' not in n.data:
            print("\nSorry, we don't have cats available for adoption!!\n")
        else:
            print("\nAdopting an oldest Cat!!\n")
            print(adoptCat)
            self.printll()


    def createlist(self,ll):
        self.head = Node()
        for elem in ll:
            self.enqueue(elem)
            
    def printll(self):
        n=self.head.next
        print_list=[]
        while n!=None:
            print_list.append(n.data)
            n=n.next
        #print(print_list)
        print(" -> ".join(print_list))


sll = AnimalShelter()
#ll = ['d1','c1','d2','d3','c3','c4','c5','d4','d5']
#sll.createlist(ll)
sll.enqueue('d1')
sll.enqueue('c1')
sll.enqueue('d2')
sll.enqueue('d3')
sll.enqueue('c3')
sll.enqueue('c4')
sll.printll()

sll.adopt('Dog')
sll.adopt('Cat')
sll.adopt('Any')

sll.enqueue('c5')
sll.enqueue('c6')
sll.enqueue('c7')

sll.printll()

sll.adopt('Cat')
sll.adopt('Cat')
sll.adopt('Cat')
sll.adopt('Dog')
sll.adopt('Dog')
sll.adopt('Any')
sll.adopt('Dog')
sll.adopt('Cat')
sll.adopt('Cat')
#sll.dequeueAny()
#sll.dequeueDog()
#sll.dequeueCat()





        
