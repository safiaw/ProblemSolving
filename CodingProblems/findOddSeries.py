

#Assumption:
#Exactly one will be an odd string

def computeDistancePattern(string):

    dp=''
    l=len(string)-1
    for index in range(0,l):
        dis=ord(string[index+1])-ord(string[index])
        dp+=str(dis)
    return dp

def findOddSeries(strings):

    dp1 = computeDistancePattern(strings[0])
    dp2 = computeDistancePattern(strings[1])
    for index in range(2,len(strings)):
        cdp = computeDistancePattern(strings[index])
        if cdp==dp1 and cdp==dp2:
            continue
        elif cdp==dp1 and cdp!=dp2:
            return strings[1]
        elif cdp!=dp1 and cdp==dp2:
            return strings[0]
        else:
            return strings[index]

if __name__=="__main__":

    #strings = ['ABCD','BCDE','EFGH','DCBE']
    strings = ['ACB','BDC','CED','DEF']
    oddstring = findOddSeries(strings)
    print(oddstring)

'''
Use cases

Given:
string series[n]
 3 <= n <= 26
 2<= length of element <= 26
 list will have exactly one odd string

take extreme cases

# list with 3 strings
# list with 26 strings
# list with strings of size 2
# list with strings of size 26

take intermediate cases
# list with strings each in sequence ascending order
# list with strings each in sequence descending order
# list with distane positive
# list with distance negative
# list with distance 1
# list with distance greater than 1
'''



