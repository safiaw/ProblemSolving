import queueArray

class Node:

    def __init__(self,elem=None):

        self.data=elem
        self.parent=None
        self.left=None
        self.right=None

class minheap:

    def __init__(self):
        self.root=None
    
    def insertintocbt(self,elem):
        
        if self.root==None:
           self.root=Node(elem)
           return self.root
        
        else:
            
           n=self.root

           while n!=None:

              #sibling = n.parent.right
              if n.left==None and n.right==None:
                  n.left = Node(elem)
                  n.left.parent = n
                  return n.left
                  
              elif n.left!=None and n.right==None:
                  n.right = Node(elem)
                  n.right.parent = n
                  return n.right

              elif n.left!=None and n.right!=None:

                if n.parent!=None:
                  if n.parent.right!=None:
                     sibling=n.parent.right
                     if sibling.left==None and sibling.right==None:
                        sibling.left = Node(elem)
                        sibling.left.parent = sibling
                        return sibling.left

                     elif sibling.left!=None and sibling.right==None:
                        sibling.right = Node(elem)
                        sibling.right.parent = sibling
                        return sibling.right

                     elif sibling.left!=None and sibling.right!=None:
                        n=n.left
                else:
                     n=n.left


    def insertintominheap(self, elem):
       
        insertednode=self.insertintocbt(elem)
        print("Printing tree after inserting %d" %(insertednode.data))
        if insertednode.parent!=None:
            if insertednode.data < insertednode.parent.data:
               self.fixminheap(insertednode) 
        self.inorder(self.root)
    
    def fixminheap(self, n):
        
        while n.parent!=None:
              if n.data < n.parent.data:
                  temp = n.data
                  n.data = n.parent.data
                  n.parent.data = temp
              n = n.parent
              
    def swap(self,n1,n2):

        temp = n1
        n1 = n2
        n2 = temp
        return
        
        
   
    def extractmin(self,size):

        minm = self.root.data

        # find last element in the tree - bottommost rightmost
        # level order traversal such as BFS will help find the last element
        # find the height of the subtree and move to the subtree with larger height
        visited=[]
        bqueue = queueArray.myQueue(size)
        firstnode = self.root
        bqueue.insert(firstnode)

        while not bqueue.isEmpty():

            node = bqueue.remove()
            visited.append(node)

            if node.left!=None and node.right!=None:
                if node.left not in visited:
                    bqueue.insert(node.left)
                if node.right not in visited:
                    bqueue.insert(node.right)
                    
            if node.left!=None and node.right==None:
                if node.left not in visited:
                    bqueue.insert(node.left)
                    
        print("Printing level order traversal of the tree\n")        
        for node in visited:
            print(node.data)
      
        lastnode = visited[-1]

        lastelem = lastnode.data
        
        self.root.data = lastelem
        
        if lastnode.parent.right == lastnode:
            lastnode.parent.right=None
        else:
            lastnode.parent.left=None

        print("Printing tree after removing minimum element and swapping it with last element\n")
        self.inorder(self.root)
        
        # place the root node at its proper position
        n=self.root
        while n!=None:
          print(n.data)
          if n.left!=None and n.right!=None:              
            if n.data > n.left.data and n.data > n.right.data:
                minmval = min(n.left.data,n.right.data)
                if minmval == n.left.data:
                    temp = n.data
                    n.data = n.left.data
                    n.left.data = temp
                    #self.swap(n.data,n.left.data)
                    n=n.left
                else:
                    temp = n.data
                    n.data = n.right.data
                    n.right.data = temp
                    #self.swap(n.data,n.right.data)
                    n=n.right
            elif n.data > n.left.data and n.data < n.right.data:
                    temp = n.data
                    n.data = n.left.data
                    n.left.data = temp
                    #self.swap(n.data,n.left.data)
                    n=n.left
            elif n.data > n.right.data and n.data < n.left.data:
                    temp = n.data
                    n.data = n.right.data
                    n.right.data = temp
                    #self.swap(n.data,n.right.data)
                    n=n.right
          elif n.left!=None and n.right==None:
             if n.data > n.left.data:
                 temp = n.data
                 n.data = n.left.data
                 n.left.data = temp
                 #self.swap(n.data,n.left.data)
                 n=n.left
          elif n.left==None and n.right==None:
              break
            
            
        print("Printing tree after placing the root node to its proper position\n")
        self.inorder(self.root)
        return minm

    def inorder(self, n):

        if n!=None:
           self.inorder(n.left)
           print(n.data)
           self.inorder(n.right)


mheap = minheap()
mheap.insertintominheap(50)
mheap.insertintominheap(55)
mheap.insertintominheap(80)
mheap.insertintominheap(90)
mheap.insertintominheap(10)
mheap.insertintominheap(12)
mheap.insertintominheap(6)
mheap.insertintominheap(2)

print("Hi!! Please have a look on your min-heap tree\n")
mheap.inorder(mheap.root)

#print("Minimum element in the tree is : %d" %(mheap.extractmin()))

#mheap.inorder(mheap.root)

print("Extracting minimum element from the minheap tree\n")
minm=mheap.extractmin(8)

print("Minimum element in the tree is : %d" %(minm))

mheap.inorder(mheap.root)




