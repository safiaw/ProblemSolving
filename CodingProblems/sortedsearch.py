

class Listy:


      def __init__(self):
          self.arr=[]
          self.i=0


      def insert(self,elem):
          self.arr.append(elem)
          self.i+=1

      def elementAt(self,ind):

          if 0<=ind and ind < self.i:
              return self.arr[ind]
          else:
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


      

listy = Listy()
listy.insert(1)
listy.insert(2)
listy.insert(3)
listy.insert(3)
listy.insert(4)

elem=1

i=0
while listy.elementAt(i)!=-1:
    i+=1

lastind=i-1
firstind=0
res=binarysearch(listy.arr,elem,firstind,lastind)
if res!=-1:
    print("Element found at index %d: %d" %(res,listy.elementAt(res)))
else:
    print("Sorry,element not found!!")
        
        

    
