

def oneAway(s1,s2):
    l1=len(s1)
    l2=len(s2)
    edited_str=[]
    i=0
    j=0
    nedits=0
    while i<l1:
      if j<l2:
        if s1[i]==s2[j]:
               edited_str.append(s1[i])
               i+=1
               j+=1

        else:
            if l1-l2==1:
               nedits+=1
               i+=1
            elif l1==l2:
                edited_str.append(s2[j])
                nedits+=1
                i+=1
                j+=1
      else:
          break
    print("".join(edited_str))

    if nedits<=1:
        print(True)
    else:
        print(False)

s1='pale'
s2='ple'

oneAway(s1,s2)


                
               
