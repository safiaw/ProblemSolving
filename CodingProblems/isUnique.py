
def isUnique(s):
    flag=False
    ht = {}
    l = len(s)
    
    for each_char in s:
         value = int(ord(each_char) % l)
         if value in ht.keys() and each_char in ht[value]:
             flag=False
             return flag
         elif value in ht.keys() and each_char not in ht[value]:
              ht[value].append(each_char)
              flag=True
         else:
              ht[value]=[]
              ht[value].append(each_char)
              flag=True
             
    return flag

s='abcdefghijklmnopqrstuvwxyz'
res=isUnique(s)
print(res)
