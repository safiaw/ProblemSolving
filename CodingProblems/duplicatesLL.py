
class Node():

    def __init__(self,value=None):
        self.data=value
        self.next=None

class SLL():

    def __init__(self):
        self.head=None

    def addNode(self,data):
        # add node at the end of the list
        end=Node(data)
        n=self.head
        while n.next!=None:
              n=n.next
        n.next=end
          
    def removeNode(self):
        pass
    def createlist(self,ll):
        self.head = Node()
        for elem in ll:
            self.addNode(elem)
            
    def printll(self):
        n=self.head.next
        print_list=[]
        while n!=None:
            print_list.append(n.data)
            n=n.next
        #print(print_list)
        print(" -> ".join(print_list))
    
    def removeduplicates(self):
        ht=[]
        n=self.head.next
        while n!=None:
            if n.data not in ht:
                ht.append(n.data)
                prev=n
            else:
                #remove duplicate node
                prev.next=n.next
            n=n.next
                
    def kthtolast(self,k,l):
        #for every 1 move of p1, p2 takes k moves
        # if k moves of p2 are not possible then p2 takes 1 move and p1 as is
        #length of ll is known
        # this logic is working when l contains only one k moves of p2
        # Not working for multiple k moves of p2
        p1=self.head
        p2=self.head
        i=l
        while i>0:
            if i >= k:
                # p2 takes k moves for every 1 move of p1
                j=k
                while j>0:
                    p2=p2.next
                    j-=1
                p1=p1.next
                i-=k
            else:
                # p2 and p1 both take 1 move
                p2=p2.next
                p1=p1.next
                i-=1
                        
        print(p2.data)        
        print(p1.data)

    def kthtolast1(self,k,l):
        i=l
        p=self.head.next
        while i!=k:
            p=p.next
            i-=1
        print(p.data)

    def deletemiddlenode(self,midelem):
        p=self.head
        while p.next.data!=midelem:
            p=p.next
        p.next=p.next.next
        

    def partition(self,x):
        n=self.head.next
        x=int(x)
        while n.next!=None:
            if n==self.head.next and int(n.data) < x:
                n=n.next
            elif int(n.data) >= x and int(n.next.data) < x:
                temp = n.next.next
                n.next.next = self.head.next
                self.head.next = n.next
                n.next = temp
                
            elif int(n.data) >= x and int(n.next.data) >= x:
                n=n.next
        #print(self.head.next.data)     
                
    def sumlists(self,sll2):
        
        n1=self.head.next
        n2=sll2.head.next
        sumval=0
        carry=0
        reslist=[]
        while n1!=None or n2!=None:
              elem1=int(n1.data) if n1 else 0
              elem2=int(n2.data) if n2 else 0
              
              val = elem1+elem2+carry
              if val-10 >= 0:
                  sumval=val-10
                  carry=1
              else:
                   sumval=val
                   carry=0
              reslist.append(str(sumval))
              n1 = n1.next if n1 else None
              n2 = n2.next if n2 else None  
        if carry:
            reslist.append(str(carry))
        return reslist
    
    def palindrome(self):

        ht={}
        n=self.head.next
        l=0
        while n!=None:
            if n.data not in ht.keys():
                ht[n.data]=0
                ht[n.data]+=1
            else:
                ht[n.data]+=1
            l+=1
            n=n.next
            
        print(ht)
        if len(ht.values())==1:
            return True
        
        htval=list(ht.values())[0:-1]
        if l%2==0:
            if sum(htval) == 2*len(htval):
                return True
            else:
                return False
        else:
            last_val=list(ht.values())[-1]
            if sum(htval) == 2*len(htval) and last_val==1:
                return True
            else:
                return False
         
    def intersection(self,sll2):
        ht=[]
        n1=self.head.next
        n2=sll2.head.next

        while n1.next!=None:

            if n1 not in ht:
                ht.append(n1)
            else:
                return n1
            n1=n1.next
            
        while n2.next!=None:

            if n2 not in ht:
                ht.append(n2)
            else:
                return n2
            n2=n2.next
        return None        # no intersecting node by reference
                    
        
    def loopdetection(self):

    def createCLL(self,ll):
        self.head=Node()
        n=self.head
        for elem in ll:
            endnode=Node(elem)
            n.next=endnode
            n=n.next
        

ll=['a','a','a']
#['m','a','d','a','m']
#['2','8','9','6','4','3']
#['3','5','8','5','10','2','1']
#['a','b','c','d','e','f']
#['a','b','c','d','d','e','f','g','f','i','g']
#['a','b','e','k','z','r','p','l','m','n','o','q']
#['a','b','c','d']      #['a','b','c','d','d','e','f','g','f','i','g']

sll = SLL()
sll.createlist(ll)
    
#sll.printll()
#sll.removeduplicates()
#print("\n\n\n")
#sll.printll()

#sll.printll()
#sll.kthtolast1(4,11)

#sll.printll()
#sll.deletemiddlenode('c')
#sll.printll()

#sll.printll()
#sll.partition('7')
#sll.printll()


'''
# sum of two numbers in reverse order

ll1=['7','1']
ll2=['5','9']
    
sll1=SLL()
sll1.createlist(ll1)

sll2 = SLL()
sll2.createlist(ll2)

sll1.printll()
sll2.printll()

res=sll1.sumlists(sll2)
#print(res)
sll1.createlist(res)
sll1.printll()
'''
res=sll.palindrome()
print(res)


    
        
 

    
