

def peaksandvalleys(inparr):

    lt=len(inparr)
    peaks=[]
    valleys=[]
    i=0
    while i < lt:
        
        l=i-1 if i!=0 else -1
        r=i+1 if i!=lt-1 else -1

        if l!=-1 and r!=-1:
            #print("Hello!!")
            if inparr[i] <= inparr[l] and inparr[i] <= inparr[r]:
                valleys.append(inparr[i])
            elif inparr[i] >= inparr[l] and inparr[i] >= inparr[r]:
                peaks.append(inparr[i])
                
        elif l==-1:    # for first element, only right neighbor exists

            if inparr[i] <= inparr[r]:
                valleys.append(inparr[i])
            elif inparr[i] >= inparr[r]:
                peaks.append(inparr[i])
        elif r==-1:   # for last element, which has only left neighbor
            
            if inparr[i] <= inparr[l]:
                valleys.append(inparr[i])
            elif inparr[i] >= inparr[l]:
                peaks.append(inparr[i])

        i+=1

    print(peaks)
    print(valleys)
    i=0
    j=0
    k=0
    p=len(peaks)
    v=len(valleys)

    while i < p or j < v:

      if i<p:
        inparr[k]=peaks[i]
        k+=1
        i+=1
      if j<v:
        inparr[k]=valleys[j]
        k+=1
        j+=1

#inparr=[5,8,6,2,3,4,6]
inparr=[5,3,1,2,3]
peaksandvalleys(inparr)
print(inparr)


