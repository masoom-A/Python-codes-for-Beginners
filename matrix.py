import math
print("enter size of matrix")
n=int(input())
m=[]
arr=[]
hg_sum=0
for _ in range(n):
    m.append(list(map(int,input().split())))
for i in range(0,n-2):
    for j in range(0,n-2):
        hg_sum+=sum(m[i][j:j+3])
        hg_sum+=sum(m[i+1][j+1:j+2])
        hg_sum+=sum(m[i+2][j:j+3])
        arr.append(hg_sum)
        hg_sum=0
arr.sort()
print(arr[-1])


    
        
    
    
    
