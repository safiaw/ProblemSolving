

def nextsmallestandlargest(n):

    lbits = len(bin(n))-2
    count=0
    while n!=0:
        n = n & (n-1)
        count+=1

    nsmallest = (1 << count ) - 1
    nlargest = nsmallest << (lbits-count)

    return nsmallest,nlargest

n = 19
ns,nl = nextsmallestandlargest(n)
print("The number is %d and its binary representation is %s" %(n,bin(n)))
print("The next smallest number is %d and its binary representation is %s" %(ns,bin(ns)))
print("The next largest number is %d and its binary representation is %s" %(nl,bin(nl)))
    
