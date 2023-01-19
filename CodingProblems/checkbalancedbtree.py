
#from math import abs

class Node:

    def __init__(self,elem=None):

        self.data=elem
        self.left=None
        self.right=None


def checkbalancedbtree(node):

    if node!=None:
       if node.left==None and node.right==None:
          return 0

       else:
          leftht = 1 + checkbalancedbtree(node.left)
          rightht = 1 + checkbalancedbtree(node.right)

          nodeht = abs(leftht-rightht) 
        
          return nodeht
          #if nodeht > 1:
          #   print("Tree is not balanced\n")
          #   return nodeht
          #else:
          #   print("Tree is balanced\n")
          #   return nodeht
    else:
       return 0


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)


res=checkbalancedbtree(root)
print(res)
if res > 1:
    print("\n\n Tree is not balanced \n\n ")
else:
    print("\n\n Tree is balanced \n\n")

#print(res)

