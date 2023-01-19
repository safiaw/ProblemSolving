import queueArray

graphadj={0:[1,2,4],1:[2,5],2:[3,5],3:[5],4:[],5:[]}

#{0:[1,4,5],1:[3,4],2:[1],3:[2,4],4:[],5:[]}
bqueue = queueArray.myQueue(len(graphadj))


def bfs(source, target):
    
    path=[]
    if source == target:
        return False
    else:
        if target in graphadj[source]:
            path.append(source)
            path.append(target)
            print(path)
            return True
        else:
            
            visited = []
            bqueue.insert(source)

            while not bqueue.isEmpty():

                  elem = bqueue.remove()
                  visited.append(elem)
                  if elem != target and graphadj[elem]==[]:
                      pass
                  elif elem == target:
                      path.append(elem)
                      break
                  else:
                     for ndnbr in graphadj[elem]:
                         if ndnbr not in visited and ndnbr not in bqueue.array:
                                bqueue.insert(ndnbr)
                     
                     path.append(elem)
            print(path)
            return True

#bfs(0,5)
#bfs(0,5)
print("\n")
bfs(0,1)
print("\n")
bfs(0,2)
print("\n")
bfs(0,3)
print("\n")
bfs(0,4)
print("\n")
bfs(0,5)
            
         
         

