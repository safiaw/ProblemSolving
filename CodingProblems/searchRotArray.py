
def binarysearch(arr,elem,l,h):

    ## taking array elements by using index and search within
    
    if l>h:
        return -1
    
    m=(l+h)//2
    #print(arr)
    print(m,arr[m])
    
    if arr[m]==elem:
       return m
    elif elem < arr[m]:
       return binarysearch(arr,elem,l,m-1)

    elif elem > arr[m]:
       return binarysearch(arr,elem,m+1,h)



def searchRotArray(inparr,elem):

    l=len(inparr)
    i=0
    startpos=i
    stoppos=i
    while i < l-1:
        
        if inparr[i]>inparr[i+1] or i==l-2:
            
            stoppos=i if i!=l-2 else i+1
            print(startpos,stoppos)
            res=binarysearch(inparr,elem,startpos,stoppos)
            print(res)
            if res!=-1:
                return res
            
            startpos=stoppos+1
            
        i+=1
    return -1


inparr=[15,16,19,20,25,1,3,4,5,7,10,14]
elem=3
res=searchRotArray(inparr,elem)
if res!=-1:
    print("Element found at index %d: %d" %(res,inparr[res]))
else:
    print("Sorry,element not found!!")
            
            
