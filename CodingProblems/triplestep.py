
def bstriplestep(n):

    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return bstriplestep(n-1) + bstriplestep(n-2) + bstriplestep(n-3)
        


def triplestep(n):   

    if n==1:       # what about case when n=0 and when n<0 assuming n is an integer
        return 1
    elif n==2:
        return triplestep(n-1) + 1
    elif n==3:
        return triplestep(n-1) + triplestep(n-2) + 1
    else:
        return triplestep(n-1) + triplestep(n-2) + triplestep(n-3)


hm={}
hm[0]=1

def dptriplesteptd(n):

    if n < 0:
        return 0
    else:
        if n not in hm.keys():
            hm[n] = dptriplesteptd(n-1) + dptriplesteptd(n-2) + dptriplesteptd(n-3)
        return hm[n]

def dptriplestepbu(n):

    if n < 0:
        return 0
    else:   
        fv=0
        sv=0
        tv=1
        i=1
        while i<=n:
            cv = fv+sv+tv
            fv=sv
            sv=tv
            tv=cv
            i+=1
        return cv
    

    

n=5
#res=triplestep(n)
#res=dptriplesteptd(n)
res=dptriplestepbu(n)
print("For reaching %d steps, %d possible ways exists" %(n,res))
