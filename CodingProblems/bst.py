
class Node:

    def __init__(self,elem=None):

        self.data=elem
        self.left=None
        self.right=None


def createbst(datalist):

    root=None
    
    for elem in datalist:
               
        if root==None:
           root=Node(elem)
        else:
           n=root
           while n!=None:
               #print(n.data)
               if elem > n.data:
                  if n.right!=None:
                     n=n.right
                  else:
                     n.right=Node(elem)
                     break
               else:
                  if n.left!=None:
                     n=n.left
                  else:
                     n.left=Node(elem)
                     break
    
    return root

def preorder(n):

    if n!=None:
       print(n.data)
       preorder(n.left)
       preorder(n.right)

def inorder(n):

    if n!=None:
       inorder(n.left)
       print(n.data)
       inorder(n.right)

def postorder(n):

    if n!=None:
       postorder(n.left)
       postorder(n.right)
       print(n.data)


dl=[9,3,8,4,11,7,15,6,1]
root=createbst(dl)
print("Hi there!! Here's the preorder traversal for you\n\n")
preorder(root)

print("Hi there!! Here's the inorder traversal for you\n\n")
inorder(root)

print("Hi there!! Here's the postorder traversal for you\n\n")
postorder(root)


