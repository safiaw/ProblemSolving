# TC=O(n)
# SC=O(n)- a hashtable is used


def palindromePermut(s):

    ht={}

    for each_char in s:
        each_char = each_char.lower()
        if each_char==' ':
           continue
        elif each_char not in ht.keys():
            ht[each_char]=0
            ht[each_char]+=1
        else:
            ht[each_char]+=1
    print(ht)

    s.replace(' ','')
    if len(s) % 2 != 0:
       val=list(ht.values())[0:-1]
       last_val = list(ht.values())[-1]
       if sum(val) == 2*len(val) and last_val==1:
           return True
       else:
           return False
    if len(s)%2==0:
        val=list(ht.values())[0:-1]
        if sum(val) == 2*len(val):
            return True
        else:
            return False


s="Madam"      #"Tact Coa"
res = palindromePermut(s)
print(res)
