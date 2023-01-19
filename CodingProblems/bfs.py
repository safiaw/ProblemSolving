import queueArray

graphadj={0:[1,4,5],1:[3,4],2:[1],3:[2,4],4:[],5:[]}
bqueue = queueArray.myQueue(len(graphadj))


def bfs():
    visited = []
    firstnode = list(graphadj.keys())[0]
    bqueue.insert(firstnode)

    while not bqueue.isEmpty():

         elem = bqueue.remove()
         print(elem)
         visited.append(elem)

         if graphadj[elem] != []:
            for ndnbr in graphadj[elem]:
                if ndnbr not in visited and ndnbr not in bqueue.array:
                      bqueue.insert(ndnbr)
      

bfs()

