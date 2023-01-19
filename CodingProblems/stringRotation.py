
def isSubstring(s,s1):




def checkrotation(s1,s2):

    l1=len(s1)
    l2=len(s2)

    if l1 != l2:
        return False
    elif s1==s2 and l1!=1 and l2!=1:
        return False
    elif s1==s2 and l1==1 and l2==1:
        return True
    else:
        i=l2
        j=0
        flag=False
        while i>0:

            if s2[i]!=s1[j]:
                i-=1
            else:
                j+=1
                pos=i-1
                flag=True
                while i <l2:
                    if s1[j]==s2[i]:
                        i+=1
                        j+=1
                        flag=True

                    else:
                        flag=False
                        break

            if flag:
                  res=isSubstring(s2[0:pos],s1)
                  if res:
                      return True
                  else:
                      return False
            else:
                return False

s1=""
s2=""
print(checkrotation(s1,s2))
                        
 
