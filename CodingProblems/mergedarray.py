

def mergedarray(bigarr,smallarr):

    l=len(bigarr)-1
    s=len(smallarr)-1
    b=l-s-1
    i=l      
    while b>-1 and s>-1:
        
        #print(bigarr[b],smallarr[s])

        if bigarr[b] > smallarr[s]:
           print("Biggie wins!!")
           bigarr[i]=bigarr[b]
           b-=1
           i-=1
        elif bigarr[b] < smallarr[s]:
           print("Small wins!!")
           bigarr[i]=smallarr[s]
           s-=1
           i-=1
        #print(bigarr)
    while b>-1:
        bigarr[i]=bigarr[b]
        i-=1
        b-=1
    while s>-1:
        bigarr[s]=smallarr[s]
        i-=1
        s-=1


a=[10,14,19,21,0,0,0,0,0]
b=[1,3,4,5,6]

mergedarray(a,b)
print(a)
