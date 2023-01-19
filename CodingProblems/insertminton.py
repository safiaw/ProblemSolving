


def insertminton(n,m,i,j):


    if len(bin(n))==len(bin(m)):   ## converting int to binary and them computing length of binary number is COSTLY
       return m

    elif i==j:

       mask = ~(1 << i)
       return (n & mask) | (m << i)

    else:

       mask = pow(2,(j-i+1))-1     ## a costly operation - calculating power of 2
    
       mask = ~(mask << i)

       n = (n & mask) | (m << i)
    
       return n

n = 12
m = 14
j=1
i=1
res = insertminton(n,m,i,j)
print("The number after inserting m into n is %d and its binary is %s" %(res,bin(res)))


    




