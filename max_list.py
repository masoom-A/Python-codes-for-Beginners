import math
def maximum(list):
    max=list[0]
    for x in list:
        if x>max:
           max=x
    print(max)
    
n=int(input("enter the range"))
list=[]
for x in range(n):
    ele=int(input())
    list.append(ele)
maximum(list)

