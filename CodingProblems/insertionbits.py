

def insertMintoN(N,M,i,j):

    k=0
    while i <=j:

        v = M & (1<<k)
        k+=1
        mask = ~(1<<i)
        N = N & mask
        N = N | (v << i)
        i+=1
    return N

N=19
M=3
i=2
j=3
res=insertMintoN(N,M,i,j)
print(bin(res))
