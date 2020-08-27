def func(list1):
    print("the maximum element is ",max(list))
    reslt=0
    for sum in list:
        reslt=reslt+sum  
    return reslt
list=[]
for x in range (5):
    ele=int(input())
    list.append(ele)
    
print("the addition is",func(list))
