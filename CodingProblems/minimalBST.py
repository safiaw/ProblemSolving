
from math import ceil

class Node:

    def __init__(self,elem=None):

        self.data=elem
        self.left=None
        self.right=None

class minimalBST:

    def __init__(self):

        self.root=None

    def createBST(self,arr):

        l = len(arr)
        if l==0:
           return None
        
        elif l==1:
           node = Node(arr[0])
           #print(node.data)
           return node
        
        elif l>1:
            mid = int(ceil((l-1)/2)) if l%2==0 else int((l-1)/2)
            data = arr[mid]
            
            node = Node(data)
            if self.root==None:
                self.root=node
            node.left = self.createBST(arr[0:mid])
            node.right = self.createBST(arr[mid+1:l])
            
            return node
                         

    def inorder(self,n):

        if n!=None:
            
            self.inorder(n.left)
            print(n.data)
            self.inorder(n.right)
              

arr=[1,3,9,11,23,50,99]
mbst = minimalBST()
mbst.createBST(arr)
mbst.inorder(mbst.root)
