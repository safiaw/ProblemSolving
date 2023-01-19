
def insertionsort(inparray):

    l = len(inparray)

    for i in range(1,l):
        key = inparray[i]
        inserted=False
        for j in range(i-1,-1,-1):

            if key < inparray[j]:
                inparray[j+1] = inparray[j]
  
            else:
                inparray[j+1] = key
                inserted=True
                break
    
        if not inserted:
           inparray[j]=key
        print(inparray)

#inparray = [10,0,12,-1,8,-4,16]
inparray = [9,5,1,4,3]
insertionsort(inparray)
print(inparray)

