"""
tree
root, company
each node - a car distributor that recieves cars from the parent node and ship it to its children nodes

leaf nodes - car dealerships - consumers

value at each node - int - cost of shipping a car

sales path - branch from root to a leaf
cost - sum of node values in the path




"""

def dfs(currNode, salesPathCost, minimalPathCost):
    
    if len(currNode.children) == 0 and salesPathCost < minimalPathCost:
          #print(salesPathCost)
          minimalPathCost = salesPathCost
          print("Completed one path", salesPathCost, minimalPathCost)
          
    for children in currNode.children:
         #print(children.cost)
         dfs(children, children.cost + salesPathCost, minimalPathCost)

def dfs1(rootNode):
    stack = [[rootNode, rootNode.cost]]
    salesPathCost = 0
    minimalPathCost = float("inf")
    while len(stack):
          [currNode, salesPathCost] = stack.pop()
          #print(salesPathCost)
          print(minimalPathCost)
          if currNode.children == [] and salesPathCost < minimalPathCost:
                  minimalPathCost = salesPathCost 
                  continue
          for children in currNode.children:
              stack.append([children, salesPathCost + children.cost])
    return minimalPathCost   
             

def get_cheapest_cost():
  #pass # your code goes here
  rootNode = Node(0, [Node(5, [Node(4, [])]), Node(3,[Node(2,[Node(1, [Node(1,[])])]), Node(0, [Node(10,[])])]), Node(6, [Node(1, []), Node(5, [])])])
  minimalPathCost = float("inf")
  dfs(rootNode, rootNode.cost, minimalPathCost)
  print(minimalPathCost)
  #return dfs1(rootNode)

class Node:

  # Constructor to create a new node
  def __init__(self, cost, children):
    self.cost = cost
    self.children = children
    self.parent = None

print(get_cheapest_cost())
