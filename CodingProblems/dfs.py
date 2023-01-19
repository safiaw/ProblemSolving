import stackInArray

graphadj={0:[5,4,1],1:[4,3],2:[1],3:[4,2],4:[],5:[]}

dstack = stackInArray.stackArray(len(graphadj))

def dfs():

    visited=[]
    firstnode = list(graphadj.keys())[0]
    dstack.push(firstnode)

    while not dstack.isEmpty():
         
          elem = dstack.pop()
          print(elem)
          visited.append(elem)
          if graphadj[elem] != []:
             for ndnbr in graphadj[elem]:
                 if ndnbr not in visited and ndnbr not in dstack.array:
                    dstack.push(ndnbr)
         
dfs()




