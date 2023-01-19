
def fact(n):

   if n==1:
       return 1
   else:
       return n*fact(n-1)


def permutation(arr):

    l=len(arr)
    if l==1:
        return
    elif len(all_permutations)==totalperm:
        return
    
    else:
        
        for i in range(0,l):
           
           for j in range(0,l):
              new_arr=arr.copy()
              if i!=j:
                temp=new_arr[i]
                new_arr[i]=new_arr[j]
                new_arr[j]=temp
                #print(new_arr)
                if new_arr not in all_permutations:
                   all_permutations.append(new_arr)
                   #print(all_permutations)
                   permutation(new_arr)
                   return 

    
arr=[1,4,8,9]
#arr=[3,6]
#arr=[2]
#arr=[1,4,9]
l=len(arr)
totalperm=fact(l)

print(totalperm)


all_permutations = []

all_permutations.append(arr)
print(all_permutations)

permutation(all_permutations[0])

print(all_permutations)
print(len(all_permutations))

