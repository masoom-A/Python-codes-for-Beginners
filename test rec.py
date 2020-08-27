import  sys
sys.setrecursionlimit(1000)
def rec(l,i):
    
    print(l, end="")
    i+=1
    rec(l,i)
i=0   
l="firoj"
rec(l,i)
print(i)
