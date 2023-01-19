from datetime import datetime

"""
# bottom-up recursive approach
# time - O(3^n) and space - O(n)

def countWays(n):

    if n==0:
        return 1
    if n>0 and n<=2:
        return n
    return countWays(n-1) + countWays(n-2) + countWays(n-3)
"""

'''
## bottom-up with memoization
# time - O(n) and space - O(n)

def memoize(f):
    memo = {}
    def helper(index, n):
        if index not in memo:
            memo[index] = f(index, n)
        return memo[index]
    return helper


@memoize
def countWays(i, n):

    if i==n:
        return 1
    if i>n:
        return 0
    return countWays(i+1, n) + countWays(i+2, n) + countWays(i+3, n)
'''

# top-down with memoization dp without decorators
def countWays(n, memo):

    if n==0:
        return 1
    if n>0 and n<=2:
        return n
    if n not in memo:
        memo[n] = countWays(n-1, memo) + countWays(n-2, memo) + countWays(n-3, memo)
    return memo[n]

"""
# iterative approach - memoization without a map
# when order matters
def countWays(n):
    
    if n==0:
        return 1
    if n>0 and n<=2:
        return n
    
    t = [0 for _ in range(n+1)]
    
    t[0] = 1
    t[1] = 1
    t[2] = 2

    for index in range(3, n+1):
        t[index] = t[index-1] + t[index-2] + t[index-3]

    print(t, len(t))
    return t[n]
"""      
    


n=30
sTime = datetime.now()
memo = {}
result = countWays(n,memo)
print(result)
eTime = datetime.now()
print("Total time in seconds: %s" %((eTime - sTime).total_seconds()))
