
from datetime import datetime
'''
# using recursion - divide and conquer
# time - O(2^n)
# space - O(n)

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
'''

# optimizing using dp - bottom up approach
# time - O(n)
# space - O(1)
def fib(n):

    firstTerm = 0
    secondTerm = 1

    for index in range(2,n+1):  # iterative 
        thirdTerm = firstTerm + secondTerm
        firstTerm = secondTerm  # copy operation - costly
        secondTerm = thirdTerm  # copy operation - costly
    return thirdTerm

'''
# optimizing using dp - top up (memoization) approach
# using python function decorators for memoization
# time - O(n)
# space - O(n)

def memoize(f):   # decorator function
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

class Memoize:      # decorator class

   def __init__(self, f):
       self.f = f
       self.memo = {}
   def __call__(self, *args):
       if args not in self.memo:
          self.memo[args] = self.f(*args)
       return self.memo[args]

# fib = memoize(fib) - function result cache
@memoize   or @Memoize
def fib(n):  # decorated function

    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
'''
n = 100
sTime = datetime.now()
result = fib(n)
print(result)
eTime = datetime.now()
print("Total time in seconds: %s" %((eTime-sTime).total_seconds()))

