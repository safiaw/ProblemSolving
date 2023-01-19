
def getbiti(num,i):

    return (num & (1 << i))!=0


def setbiti(num,i):

    return  num | (1 << i)

def clearbiti(num,i):

    return num & ~( 1 << i)

def clearbitsfrommsbtoi(num,i):  # inclusive i

    mask = (1 << i) - 1
    return num & mask

def clearbitsfromlsbtoi(num,i):  # inclusive i
    mask = ~((1 << i+1) - 1)
    return num & mask

def updatebiti(num,i,v):
    mask = ~(1 << i)
    num = num & mask
    value = v << i
    return num | value
    
    

num=12
i=1

print("\n\nGet ith bit\n\n")
print(bin(num))
res=getbiti(num,i)
print(bin(res))

print("\n\nSet ith bit\n\n")
res = setbiti(num,i)
print(num,bin(num),i)
print(res,bin(res))

print("\n\nClear ith bit\n\n")
res = clearbiti(num,i)
print(num,bin(num),i)
print(res,bin(res))

print("\n\nClear bits from MSB to ith bit (inclusive)\n\n")
res = clearbitsfrommsbtoi(num,i)
print(num,bin(num),i)
print(res,bin(res))

print("\n\nClear bits from LSB to ith bit (inclusive)\n\n")
res = clearbitsfromlsbtoi(num,i)
print(num,bin(num),i)
print(res,bin(res))

print("\n\nUpdate ith bit with v value\n\n")
v=1
res = updatebiti(num,i,v)
print(num,bin(num),i,v)
print(res,bin(res))
