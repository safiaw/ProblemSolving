
class Node:

    def __init__(self,elem=None):

        self.data=elem
        self.left=None
        self.right=None


def sequences(node):

    result = []

    if node==None:
       result.append([])
       return result

    prefix = []
    prefix.append(node.data)
    
    leftseq = sequences(node.left)
    rightseq = sequences(node.right)

    for left in leftseq:
        for right in rightseq:

            weaved = []
            weavelists(left,right,weaved,prefix)
            result.append(weaved)
            
    return result


def weavelists(first, second, results, prefix):

    if len(first)==0 or len(second)==0:
        result = prefix.copy()
        result.extend(first[:])
        result.extend(second[:])
        results.append(result)
        return

    headfirst = first.pop(0)
    prefix.append(headfirst)
    weavelists(first,second,results,prefix)
    prefix.pop(-1)
    first.insert(0,headfirst)

    headsecond = second.pop(0)
    prefix.append(headsecond)
    weavelists(first,second,results,prefix)
    prefix.pop(-1)
    second.insert(0,headsecond)

    

'''root = Node(2)
root.left = Node(1)
root.right = Node(3)'''

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.right = Node(9)
root.right.right.left = Node(8)
root.right.right.right = Node(10)

res = sequences(root)
print(res)

                        

                
    
