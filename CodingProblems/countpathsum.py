
class Node:

    def __init__(self,elem=None):

        self.data=elem
        self.left=None
        self.right=None


def countpathsum(node,target):

    if node==None:    # if any empty tree 
        return 0

    elif node.data == target:   # if a tree has one node with the target value
        return 1
     
                         # if a tree has more than one node with the root not having the target value

    res1 = node.data + countpathsum(node.left,target)
    if res1==target:
        return 1
    return res1

    res2 = node.data + countpathsum(node.right,target)
    if res2==target:
          return 1
    return res2


def pathsumlists(node):

    if node==None:
        return []

    elif node.left==None and node.right==None:
        return [node.data]
    
    else:
        pathsuml=[]
        pathsuml.append(node.data)
        l = pathsumlists(node.left)
        if l!=[]:
            for i in range(0,len(l)):
                l[i]=node.data+l[i]
            pathsuml.extend(l)

        r = pathsumlists(node.right)
        if r!=[]:
            for i in range(0,len(r)):
                r[i]=node.data+r[i]
            pathsuml.extend(r)

        return pathsuml

root = Node(4)
root.left = Node(-1)
root.right = Node(-2)
root.left.right = Node(2)
root.left.right.right = Node(3)
root.right.right = Node(1)

#root.left.right = Node()

#root.right.left = Node()
#root.right.right = Node()
target=3
#res = countpathsum(root,target)
res = pathsumlists(root)
print(res)
   

# visit each node
# find each node paths sum list
# count occurence of target value in the list
# when all nodes are visited return the count 

    
       
