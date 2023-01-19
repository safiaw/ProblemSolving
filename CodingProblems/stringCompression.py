
def stringCompression(s):

    s.lower()
    c=''
    l=len(s)
    i=0
    count=1
    while i < l-1:      
        if s[i]!= s[i+1] and s[i+1]!='':
           char=s[i]
           c+=char+str(count)
           count=1
        else:
            char=s[i]
            count+=1

        i+=1  

    c+=char+str(count)
    print(c)

    if len(c) > l:
        return s
    else:
        return c


s="aabcccccaaa"
res=stringCompression(s)
print(res)
