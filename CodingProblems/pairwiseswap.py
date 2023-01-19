
def pairwiseswap(n):

    oddmask = 0xaaaaaaaa       # 101010101010 = 0xaaaaaaaa in hex for 32 bit number (8 hex digits)
    evenmask = 0x55555555    # 010101010101 = 0x555555 in hex for 32 bit number (8 hex digits)
    oddbits = n & oddmask
    evenbits = n & evenmask

    return (oddbits >> 1) | (evenbits << 1)

n = 22
res = pairwiseswap(n)
print("The number is %d and its binary representation is %s" %(n,bin(n)))
print("The pairwise swapped number is %d and its binary representation is %s" %(res,bin(res)))
