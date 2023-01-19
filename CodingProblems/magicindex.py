

def magicindex(A,l,h):

    if l>h:
        return None

    else:

     mid = (l+h)//2

     if mid==A[mid]:
        return mid
    
     elif mid < A[mid]:
        m=magicindex(A,l,mid-1)
        return m
     elif mid > A[mid]:
        m=magicindex(A,mid+1,h)
        return m


def duplicatesmagicindex(A,l,h):

    if l>h:
        return None
    else:
        mid = (l+h)//2

        if mid==A[mid]:
            return mid
        else:
            res=duplicatesmagicindex(A,l,mid-1)
            if res!=None:
                return res
            else:
                res1=duplicatesmagicindex(A,mid+1,h)
                if res1!=None:
                    return res1
                else:
                    return None

A1=[-2,-1,1,4,5,6,7,8,9,10,11]

A=[-6,-5,-4,-3,-2,5,6,7,8,13,16]
#res=magicindex(A,0,10)
res=duplicatesmagicindex(A1,0,10)
if res!=None:
   print("The magic index is %d and its value is %d" %(res,A1[res]))
else:
   print("No magic index exists!")



        
