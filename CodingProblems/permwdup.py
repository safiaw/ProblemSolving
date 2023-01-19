

def permutationwodup(inpstr):

    if len(inpstr)==1:
        return [ inpstr ]
    else:
        permlist = permutationwodup(inpstr[1:])
        firstchar = str(inpstr[0])
        newpermlist = []
        for each_pstr in permlist:
            newpstr = each_pstr
            lstr = len(each_pstr)

            for j in range(0,lstr+1):
                if j==0:
                    pstr = firstchar + newpstr[j:]
                elif j==lstr:
                    pstr = newpstr[:j] + firstchar
                else:
                    pstr = newpstr[:j] + firstchar + newpstr[j:]

                if pstr not in newpermlist:
                     newpermlist.append(pstr)

        return newpermlist

inpstr='abacdc'
res=permutationwodup(inpstr)
print("\nPrinting all permutations of string %s\n" %inpstr)
print(res)
print(len(res))





