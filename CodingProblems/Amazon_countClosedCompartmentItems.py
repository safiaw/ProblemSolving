#s = '|**|*|*'
#startIndices = [1, 1]
#endIndices = [5, 6]

#s = '****|**|**'
#startIndices = [1,1,1,1]
#endIndices = [5,7,8,9]

s = '||**||'
startIndices = [2,1]
endIndices = [5,5]

output = []
print(output)

for ind in range(len(startIndices)):

  currentStartInd = startIndices[ind] - 1
  currentEndInd = endIndices[ind] - 1

  stack = []
  countItems = 0
  print(currentStartInd, currentEndInd)
  for ind1 in range(currentStartInd, currentEndInd + 1):
      if s[ind1] == '|' and len(stack) == 0:
         stack.append('|')
      elif s[ind1] == '*' and len(stack) != 0:
         stack.append('*')
      elif s[ind1] == '|' and len(stack) != 0:
         while stack.pop() == '*':
               countItems += 1
         stack.append('|')
  output.append(countItems)

print(output)
