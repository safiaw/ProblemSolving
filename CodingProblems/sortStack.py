import stackArray


def sortStack(S,T,size):

 S.showstack()
 T.showstack()
 i=0
 while i < size:
    if T.isEmpty():
        maxv=S.pop()
        while not S.isEmpty():
            
            if maxv < S.peek():
               T.push(maxv)
               maxv=S.pop()
            
            else:
               elem=S.pop()
               T.push(elem)
    else:
        maxv=T.pop()
        while not T.isEmpty():
             
             if maxv < T.peek():
                S.push(maxv)
                maxv = T.pop()
             else:
                elem=T.pop()
                S.push(elem)

        while S.peek() < maxv:
              elem=S.pop()
              T.push(elem)
    S.push(maxv)
    S.showstack()
    T.showstack()
    
    i+=1
 S.showstack()
 S.peek()
    

size=6 #7
elems=[6,5,4,3,2,1] #[8,1,2,11,3,4,15]
stack = stackArray.stackArray(size)
tempstack = stackArray.stackArray(size)

for el in elems:
    stack.push(el)

sortStack(stack,tempstack,size)

#### Complexity  ###
### Time complexity is O(n^2)
### To find a largest element out of n elements, n push and pop operations are performed
### Space complexity is O(2n)
    
