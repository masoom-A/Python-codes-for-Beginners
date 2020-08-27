num=int(input("enter a number: "))
print("the divisors are")
for div in range(1,num+1):
    if num%div==0:
        print("{}".format(div))
        
    
