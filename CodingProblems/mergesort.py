import math

def mergesort(arr):

  l=len(arr)

  if l > 1:

    r=l//2;
    LS = arr[:r]
    RS = arr[r:]

    mergesort(LS)
    mergesort(RS)

    print(LS)
    print(RS)
    ls = len(LS)
    rs = len(RS)
    
    i=0
    j=0
    k=0
    while i<ls and j<rs:

        if LS[i] <= RS[j]:
            arr[k]=LS[i]
            i+=1
        else:
            arr[k]=RS[j]
            j+=1
        k+=1

    while j<rs:
            arr[k]=RS[j]
            k+=1
            j+=1
            
    
    while i<ls:
            arr[k]=LS[i]
            k+=1
            i+=1


inparr=[5,1,7,2,9,0,12]

mergesort(inparr)
print(inparr)
