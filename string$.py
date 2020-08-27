n=int(input("enter the length"))
str=""
str1=""
for char in range(0,n+1):
    ele=input()
    str=str+ele
##for x in str:
##    
##    if x not in str1:
##        
##        str1=str1+x
##    else:
##        x="$"
##        str1=str1+x
##        
##   
##print(str1)

for y in str[1:n+1:1]:
    if str[0]==y:
        y="$"
        str1=str1+y
    else:
        str1=str
print(str1)
    
    
    
    
