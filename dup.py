string=input("enter the string")
dup=[]

for x in string:
    if x not in dup:
        dup.append(x)
        
    else:
        print("{} is duplicate".format(x))
str=""
for y in dup:
    str+=y
    
print(str)
