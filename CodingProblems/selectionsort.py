
def selectionsort(inparray):

    l = len(inparray)
    #minindex = 0

    for i in range(0,l):

        minindex=i
        
        for j in range(i+1,l):

            if inparray[minindex] > inparray[j]:
                minindex=j
    
        print(minindex)
        if minindex!=i:

           temp = inparray[minindex]
           inparray[minindex] = inparray[i]
           inparray[i] = temp
        #print(inparray)
    
inparray = [10,0,11,-1,4,8,1,-2]

selectionsort(inparray)

print(inparray)


