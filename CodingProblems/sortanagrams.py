

def sortanagrams(arrstr):

    l=len(arrstr)

    i=0
    while i < l:

        j=i+1
        swappos=j
        while j < l:
            if checkanagrams(arrstr[i],arrstr[j]):
                if j-i==1:
                    swappos=j+1
                else:
                   temp=arrstr[swappos]
                   arrstr[swappos]=arrstr[j]
                   arrstr[j]=temp
                   swappos+=1
            j+=1
        i+=1

def checkanagrams(str1,str2):

    hm1 = createhashmap(str1)
    hm2 = createhashmap(str2)
    if hm1==hm2:
        return True
    else:
        return False

def createhashmap(astr):

    hm={}
    for each_char in astr:
        if each_char not in hm.keys():
            hm[each_char]=1
        else:
            hm[each_char]+=1
    return hm

inpstr = ['car','night','save','state','happy','me','arc','thing','vase','taste','brag','grab']
sortanagrams(inpstr)
print(inpstr)






