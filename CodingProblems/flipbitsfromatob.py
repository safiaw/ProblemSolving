

def nflipbitsatob(a,b):

    dbits = a ^ b
    print(dbits, bin(dbits))
    count = 0
    while dbits!=0:
        dbits = dbits & (dbits-1)
        count+=1
    #count = countones(dbits)
    return count

a = 29
b = 15
res = nflipbitsatob(a,b)
print("Number of bits need to be flipped in a to make it b is %d" %res)
