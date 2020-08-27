import sys
## sys.setrecursionlimit(10)
def recursion(n):
    if n==0:
        return 0
    else: 
        return n+ recursion(n-1)
num=5
print(recursion(num))
