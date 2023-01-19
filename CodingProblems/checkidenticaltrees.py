import queueArray

queue = queueArray.myQueue(15)


class Node:

    def __init__(self,elem=None):

        self.data=elem
        self.left=None
        self.right=None

def checkidentical(n1,n2):

    if n1==None and n2==None:
        return True
   
    elif n1!=None and n2==None:
        return False

    elif n1==None and n2!=None:
        return False

    else:

      if n1.data==n2.data:

        res1=checkidentical(n1.left,n2.left)
        res2=checkidentical(n1.right,n2.right)

        if res1 and res2 :
            return True
        else:
            return False
   

def checksubtree(t1,t2):

    visited = []
    queue.insert(t1)
    #queue.showqueue()

    while not queue.isEmpty():

        elem=queue.remove()
        visited.append(elem.data)
        print(elem.data)
        if elem.data == t2.data:
           res=checkidentical(elem,t2)
           if res:
               return True
        
        else:
          if elem.left!=None and elem.right!=None:
                if elem.left.data not in visited:
                      queue.insert(elem.left)
                if elem.right.data not in visited:
                      queue.insert(elem.right)

          elif elem.left!=None and elem.right==None:
                if elem.left.data not in visited:
                    queue.insert(elem.left)

          elif elem.left==None and elem.right!=None:
                if elem.right.data not in visited:
                    queue.insert(elem.right)
                

    return False



t1 = Node(50)
t1.left = Node(40)
t1.left.left = Node(30)
t1.left.right = Node(49)
t1.left.right.left = Node(46)
t1.left.right.right = Node(50)
t1.left.right.left.left = Node(42)
t1.left.right.left.right = Node(47)
t1.left.right.left.left.left = Node(41)
t1.left.left.left = Node(29)
t1.left.left.right = Node(38)
t1.left.left.right.left = Node(37)
t1.left.left.right.right = Node(39)
t1.left.left.right.left.left = Node(36)
t1.left.left.right.left.left.left = Node(35)


#t1 = Node(30)
#t1.left = Node(29)
#t1.right = Node(35)

t2 = Node(37)
t2.left = Node(36)
t2.left.left = Node(35)

res = checksubtree(t1,t2)
print(res)
