import queueArray

tree={0:[1,2],1:[3,4],2:[5],3:[],4:[],5:[]}
#{0:[1],1:[2],2:[3],3:[4],4:[5],5:[]}
#
bqueue = queueArray.myQueue(6)

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
        liststr=map(str,print_list)
        print(" -> ".join(liststr))
    

def dlls():

        depth=[]
        depthlls={}
        visited=[]
        d=0
        bqueue.insert(0)
        depth.append(d)
        sll=SLL()
        sll.createlist([0])
        depthlls[d]=sll

        while not bqueue.isEmpty():

            node = bqueue.remove()
            visited.append(node)
            
            
            if tree[node]!=[]:
                d=depth[node]+1
                lls=[]
                for nbr in tree[node]:
                    if nbr not in visited:
                        
                        bqueue.insert(nbr)
                        depth.append(d)
                        lls.append(nbr)
                        
                sll = SLL()
                sll.createlist(lls)
                depthlls[d]=sll
                    

            elif tree[node]==[]:
                  pass
                
                    
        print("Printing nodes at each level and their corresponding depths\n")        
        print(visited)
        print(depth)
        lls=[]
        l=len(depth)
        for i in range(0,l):
                
                if i!=l-1 and depth[i]==depth[i+1]:
                        lls.append(visited[i])
                else:
                    lls.append(visited[i])
                    sll = SLL()
                    sll.createlist(lls)
                    depthlls[depth[i]]=sll
                    lls=[]
                
                
        for each_depth in depthlls:
                print("Linked list of nodes at depth %d\n" %each_depth)
                print(depthlls[each_depth].printll())
                
        

dlls()
            
