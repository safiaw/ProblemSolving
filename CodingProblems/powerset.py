

def bfsubsets(origset):

    subsets=[]
    n = len(origset)
    i=1
    while i < n:

        j=0
        while j < n:
            nss = set()
            nss.add(origset[j])
            k=j+1
            while k < i:
                nss.add(origset[k])
                k+=1
            subsets.append(nss)
            j+=1
        i+=1
    return subsets


def recpowerset(oset):


    l=len(oset)
    if l==2:
        ss=[set(),set([oset[0]]),set([oset[1]]),set([oset[0],oset[1]])]   # a list of subsets
        return ss
    elif l>2:
        ss=recpowerset(oset[:-1])
        newss=[]
        lastelem=oset[-1]
        for each_set in ss:
            newset=each_set.copy()
            newset.add(lastelem)
            newss.append(newset)
        ss.extend(newss)
        return ss


origset=[3,5,7,8,9]
#res=bfsubsets(origset)
res=recpowerset(origset)
print("\n\nOriginal set  -  %s\n\n" %origset)
print("\n\nAnd its subsets and its length -  %s %d\n\n" %(res,len(res)))

