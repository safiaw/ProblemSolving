

def parens(n):

    if n<1:
        return []
    elif n==1:
        return ['()']
    elif n > 1:
        prlist = parens(n-1)
        if prlist!=[]:
           newprlist=[]
           for eachpr in prlist:
           
             pr1 = '(' + eachpr +')'
             if pr1 not in newprlist:
                 newprlist.append(pr1)
             pr2 = '()' + eachpr
             if pr2 not in newprlist:
                 newprlist.append(pr2)
             pr3 = eachpr + '()'
             if pr3 not in newprlist:
                 newprlist.append(pr3)
        
        return newprlist

n=4
res=parens(n)
if res!=[]:
    print("\nAll valid combinations of %d pairs of paranetheses are\n" %n)
    print(res)
else:
    print("\nNo valid combinations exists\n")
