def isToeplitz(arr):
	
  #your code goes here
  # arr =[[],[],...]
  
  if len(arr) == 0 or len(arr[0]) == 0:
        return True
  
  # visit each diagnol elements starting from head elements in first row
  nRows = len(arr)     
  nCols = len(arr[0])
  
  i = 0
  for j in range(0, nCols):   # all head elements in first row
      
      headElem = arr[i][j]
      k = i
      l = j
      while k < nRows - 1 and l < nCols - 1:
              k += 1
              l += 1
              if headElem == arr[k][l]:
                  continue
              else:
                  return False
  j = 0
  for i in range(j+1, nRows):  # all head elements in first column
        
        headElem = arr[i][j]
        k = i
        l = j
        while k < nRows - 1 and l < nCols - 1:  
                  k += 1
                  l += 1
                  if headElem == arr[k][l]:
                     continue
                  else:
                     return False
  return True

output = isToeplitz([[0]])
print(output)
