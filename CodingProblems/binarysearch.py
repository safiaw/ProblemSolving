

def itbinarysearch(arr,elem):

    h=len(arr)
    l=0

    while l<=h:
      m = (h+l)//2

      if elem == arr[m]:
          return m
      elif elem < arr[m]:
          h=m-1
    
      elif elem > arr[m]:
          l=m+1
          
    return -1



def binarysearch(arr,elem,l,h):

    ## taking array elements by using index and search within
    
    if l>h:
        return -1
    
    m=(l+h)//2

    if arr[m]==elem:
       return m
    elif elem < arr[m]:
       return binarysearch(arr,elem,l,m-1)

    elif elem > arr[m]:
       return binarysearch(arr,elem,m+1,h)



arr = [3,4,5,6,7,8,9]
ele = -2
res = binarysearch(arr,ele,0,6)
#res = itbinarysearch(arr,ele)
print(res)
if res!=-1:
   print("Element found at index %d:%d" %(res,arr[res]))
else:
   print("Element not found!")


