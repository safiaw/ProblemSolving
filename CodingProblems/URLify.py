####### Solution 1 #########

##TC - O(n)
##SC - O(n)

def URLify(s,l):

    url = []
    i=0
    while i<l:
        w=''
        while s[i]!=' ':
            w+=s[i]
            i+=1
        print(w)
        url.append(w)
        print(s[i])
        if s[i]==' ' and i<l:
            url.append('%20')
            i+=1
        
        print(i)
    print(url)
    return url
        
 
'''
def URLify(s):

    url=[]

    for each_char in s:
        word=''
        while(each_char==' '):
            word +=each_char
        url.append(word)
        url.append('%20')
    final_str = "".join(map(str,url))
    return final_str

'''

s="Mr John Smith   "
res=URLify(s,13)
print("".join(res))
