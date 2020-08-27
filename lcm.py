def lcm(x,y):
    if x>y:
        z=x
    else:
        z=y
    while(True):
        if((z%x==0)and(z%y==0)):
            lcm =z
            break
        z+=1
    return lcm
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
print(lcm(num1,num2))
