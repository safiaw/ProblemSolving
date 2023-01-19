
def quicksort(arr):

    l = len(arr)
    if l > 1:
       pivotindex = arr[l-1]
       newpivotindex = rearrange(arr, pivotindex)
       quicksort(arr[0:newpivotindex])
       quicksort(arr[newpivotindex+1:])


def rearrange(arr, pivotindex):

    k=0
    while k < pivotindex:

        for i in range(k,pivotindex):

            if arr[i] > arr[pivotindex]:
                greaterind = i
                break
        if i == pivotindex-1:
            break

        for j in range(i+1,pivotindex):

            if arr[j] < arr[pivotindex]:
                smallerind = j
                break
        if j==pivotindex-1:
            break
        
        swap(arr[greaterind],arr[smallerind])

    swap(arr[greaterind],arr[pivotindex])
    return greaterind

def swap(a,b):

    temp = a
    a = b
    b = temp

    return

inparr = [8,7,6,1,0,9,2]
quicksort(inparr)
print(inparr)
