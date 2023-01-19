class Node():

    def __init__(self,value=None):
        self.data=value
        self.next=None


class AnimalShelter():

    def __init__(self,aType):
        self.head=Node()
        self.aType=aType

    def enqueue(self,data):
        # add node at the end of the list
        end=Node(data)
        n=self.head
        while n.next!=None:
              n=n.next
        n.next=end
        self.printll()

    def dequeue(self):

        if self.head.next==None:
           print("\nSorry, we don't have any %s for adoption!!\n" %self.aType)
        else:
           animal = self.head.next.data
           self.head.next = self.head.next.next
           #self.head.next=None
           print("\nAdopting an oldest %s!!\n" %self.aType)
           print(animal)
           self.printll()
            
    def printll(self):
        n=self.head.next
        print_list=[]
        while n!=None:
            print_list.append(n.data)
            n=n.next
        print("Available %s lists are:" %self.aType)
        print(" -> ".join(print_list))

sllCat = AnimalShelter('Cat')
sllDog = AnimalShelter('Dog')
ll = ['d1','c1','d2','d3','c3','c4','c5','d4','d5']
#sll.createlist(ll)

for animals in ll:
    if 'd' in animals:
        sllDog.enqueue(animals)
    elif 'c' in animals:
        sllCat.enqueue(animals)
    else:
        print("Not a valid animal!!")
        continue

sllDog.dequeue()
sllCat.dequeue()
sllCat.dequeue()
sllDog.dequeue()
        
'''
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
sll.adopt('Cat')'''

#sll.dequeueAny()
#sll.dequeueDog()
#sll.dequeueCat()
