
class Node:

    def __init__(self,elem=None):

        self.data=elem
        self.left=None
        self.right=None
        
nodes=[]

def inorder(node):

    if node!=None:
        
       inorder(node.left)
       nodes.append(node.data)
       inorder(node.right)

def validateBST(root):

      inorder(root)
      print(nodes)
      l=len(nodes)
      for i in range(0,len(nodes)):
          if i < l-1:
             if nodes[i] <= nodes[i+1]:
                continue
             else:
                return False
      return True
           
       
root = Node(3)
root.right = Node(9)
root.left = Node(11)

res=validateBST(root)
print(res)
