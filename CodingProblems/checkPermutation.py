

def create_ht(s1):
    ht={}
    l = len(s1)
    for each_char in s1:
        #value = ord(each_char) % l
        #print(each_char,value)
        if each_char in ht.keys() and ht[each_char]!=0:
            ht[each_char]+=1
        elif each_char not in ht.keys():
            ht[each_char]=0
            ht[each_char]+=1
    print(ht)
    return ht

def checkPermutation(ht_s1,ht_s2):
    # check if s2 is a permutation of s1
    #flag=False
    if ht_s1==ht_s2:
        return True
    else:
        return False
            


s1='abcdeghiakloncqrostuvw' #'abcda'
s2='abcdefghioklnpqrstuovw' #'bcdaa'
ht_s1=create_ht(s1)
ht_s2=create_ht(s2)
res=checkPermutation(ht_s1,ht_s2)
print(res)
        
            
