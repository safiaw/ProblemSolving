

def bubblesort(inparray):

    l = len(inparray)

    for i in range(0,l):           # putting i elements at its sorted position (at the end of the list) in each ith iteration
        for j in range(1,l-i):     # comparing each element with its adjacent element and swap

            if inparray[j] < inparray[j-1]:      # sort the list in ascending order

                temp = inparray[j-1]
                inparray[j-1] = inparray[j]
                inparray[j] = temp


def optimizedbs(inparray):        # if the array is already sorted no need of sortinog

    l = len(inparray)

    for i in range(0,l):

        swapped=False
        for j in range(1,l-i):
            
            if inparray[j] < inparray[j-1]:
                #print("hello")
                temp = inparray[j-1]
                inparray[j-1] = inparray[j]
                inparray[j] = temp
                swapped = True
        if not swapped:
            break




inparray=[0,8,2,-4,11,-9,50,26,72,-12]
inparr1=[1,2,3,4,5,6,7]
#bubblesort(inparray)
#print(inparray)

optimizedbs(inparr1)
print(inparr1)




