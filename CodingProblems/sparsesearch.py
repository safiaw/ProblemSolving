
def modbinarysearch(arr,elem,l,h):

    ## taking array elements by using index and search within
    
    if l>h:
        return -1
    
    m=(l+h)//2

    if arr[m]=="":
        m = movemidtonearest(arr,m)
     
    if m==-1:
        return -1
    
    if arr[m]==elem:
           #print(arr[m])
           return m
        
    elif elem < arr[m]:
           return modbinarysearch(arr,elem,l,m-1)
        
    elif elem > arr[m]:
           return modbinarysearch(arr,elem,m+1,h)
  

def movemidtonearest(arr,m):

    length = len(arr)
    l=m-1
    r=m+1
    while l>-1 and r<length:

        if arr[l]!="":
            m=l
            return m
        elif arr[r]!="":
            m=r
            return m
        l-=1
        r+=1
    return -1
    
            
inpstr=["at","","","","ball","","","car","","","dad","",""]
elem="at"
res=modbinarysearch(inpstr,elem,0,12)
if res!=-1:
   print("Element found at index %d:%s" %(res,inpstr[res]))
else:
   print("Element not found!")
    

    
