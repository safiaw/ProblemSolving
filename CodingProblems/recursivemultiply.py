
def itrecursivemultiply(M,m):

    i=0
    n=len(bin(m))-2
    res=0
    while i < n:

        mask = 1 << i
        nm = m & mask
        if nm!=0:
            res+= M << i
            print(res)
        i+=1
    return res

def recursivemultiply(M,m,n,count,res):

     
    if count>=n:
        #print("hello, terminating!!!")
        #print(count,res)
        return res
    else:
        nm = m & (1 << count)

        if nm!=0:
            res+= M << count
            #print(res)
        count+=1
        return recursivemultiply(M,m,n,count,res)
        #print(res)
        


multiplicant = 1289
multiplier = 1256
n=len(bin(multiplier))-2
count=0
#res=itrecursivemultiply(multiplicant, multiplier)
res=recursivemultiply(multiplicant,multiplier,n,count,0)
print("\n%d * %d = %d" %(multiplicant,multiplier,res))

