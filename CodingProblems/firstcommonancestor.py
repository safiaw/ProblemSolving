
class Node:

    def __init__(self,elem=None):

        self.data=elem
        self.parent=None
        self.left=None
        self.right=None


def calculatedepth(node):

    n=node
    d=0
    while n!=None:
         d+=1
         n=n.parent
    return d


def firstcommonancestor(n1,n2):

    d1=calculatedepth(n1)
    d2=calculatedepth(n2)
    print(d1,d2)

    if d1==0 or d2==0:
        return root.data
  
    elif d1 < d2:

        while d2!=d1:
            n2=n2.parent
            d2-=1
        firstcommonancestor(n1,n2)

    elif d1 > d2:

        while d1!=d2:
              n1=n1.parent
              d1-=1
        firstcommonancestor(n1,n2)

    else:
        while n1!=n2:
            print(n1.data,n2.data)
            n1=n1.parent
            n2=n2.parent
        return n1.data
    

root = Node('a')
root.left = Node('b')
root.left.parent = root
root.right = Node('c')
root.right.parent = root

root.left.left = Node('d')
root.left.left.parent = root.left
root.left.right = Node('e')
root.left.right.parent = root.left

root.right.left = Node('f')
root.right.left.parent = root.right
root.right.left.left = Node('g')
root.right.left.left.parent = root.right.left
root.right.left.left.left = Node('h')
root.right.left.left.left.parent = root.right.left.left

res=firstcommonancestor(root.left,root.right.left.left.left)
print(res)


