import time

def nlongestseqones(n):

    lmax=0
    count=0
    flag=False
    i=0
    start = time.time()
    while i < len(n):

        if n[i]=='1':
            count+=1
        elif n[i]=='0' and flag==False:
            count+=1
            flag=True
        elif n[i]=='0' and flag==True:
            print(count)
            if count > lmax:
                lmax=count
            count=0
            flag=False
        i+=1
    end = time.time()
    print("Total elapsed time is %s" %(end-start))
    print(count)
    if count > lmax:
        return count
    else:
        return lmax


def bitswiselongseq(n,nbits):

    lmax=0
    count=0
    flag=False
    i=0
    start=time.time()
    while i < nbits:

        mask = 1 << i
        ibit = n & mask
        if ibit!=0:
            count+=1
        elif ibit==0 and flag==False:
            count+=1
            flag=True
        elif ibit==0 and flag==True:
            print(count)
            if count > lmax:
                  lmax = count
            count =0
            flag = False
        i+=1
    end = time.time()
    print("Total elapsed time is %s" %(end-start))
    print(count)
    if count > lmax:
        return count
    else:
        return lmax



#n = '111001010'
#n='1101101'
n1='100011'
n=1775
print("\n\nFinding longest sequence in normal way\n\n")
res1=nlongestseqones(n1)
print("The length of longest sequences of ones is %d" %res1)


print("\n\nFinding longest sequence using bitwise operations\n\n")
res = bitswiselongseq(n,11)
print("The length of longest sequences of ones is %d" %res)
