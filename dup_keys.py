def dic(dic1):
    list=[]
    for x in dic1.keys():
        list.append(x)
    l=len(list)
    print("length of list is",l)
    count=0
    for y in dic1.items():
        count=count+1
        print(y)
    print("the count",count)
    if(count>l):
        return ("dic1 has duplicate keys")
    elif(count==l):
        return ("dic1 has no dup keys")
    else:
        return("put the item first")
    
dicx={1:2,1:3,2:4}
print(dic(dicx))
print(len(dicx))
##print(dicx.get(1))
##print(len(dicx))
##for y in range dicx.items():
##    count=+count
##if(y>x):
##    print("dic1 has duplicate keys")
##else:
##    print("dic1 has no dup keys")
##    
##    
    
        
        
