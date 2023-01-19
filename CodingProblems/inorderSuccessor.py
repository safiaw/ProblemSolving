
class Node:

    def __init__(self, elem=None):

        self.data=elem
        self.parent=None
        self.left=None
        self.right=None

def inorder(node):

    if node!=None:
       inorder(node.left)
       print(node.data)
       inorder(node.right)

def nextnode(node):

    if node.data <= node.parent.data:          # if node is a left child and a leaf node
        if node.left==None and node.right==None:
            return node.parent.data

    elif node.data > node.parent.data:         # if a node is a right child
        if node.left==None and node.right==None:   # and its a leaf node
            n=node.parent
            while n.data < node.data:
                n=n.parent

            if n.parent==None and n.data<node.data:
               return None                    # its a last element or rightmost element of tree - no next exists
            else:
               return n.data

    if node.left!=None and node.right!=None:   # its an internal node

          if node.right!=None:
             if node.right.left==None and node.right.right==None:    # its a leaf node
                 return node.right.data
             else:
                 n=node.right
                 while n.left!=None:
                     n=n.left

                 return n.data
          else:
             return node.parent.data

root = Node(50)
root.left = Node(40)
root.left.parent = root

root.left.left = Node(25)
root.left.right = Node(46)

root.left.left.parent = root.left
root.left.right.parent = root.left

root.left.left.left = Node(10)
root.left.left.right = Node(29)

root.left.left.left.parent = root.left.left
root.left.left.right.parent = root.left.left


root.left.left.left.left = Node(1)
root.left.left.left.right = Node(15)

root.left.left.left.left.parent = root.left.left.left
root.left.left.left.right.parent = root.left.left.left

root.left.left.right.left = Node(26)
root.left.left.right.right = Node(35)

root.left.left.right.left.parent = root.left.left.right
root.left.left.right.right.parent = root.left.left.right

inorder(root)
node = root
res=nextnode(node)
print("Inorder successor of %d is %d" %(node.data,res))
