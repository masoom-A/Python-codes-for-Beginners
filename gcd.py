def gcd(n1=2,n2=4):
    if(n1>n2):
       for x in range(n2,1,-1):
           if((n1%x==0) and (n2%x==0)):
               print(x)
               x=x-1
               break
           else:
               for x in range(n1,1,-1):
                   if((n1%x==0) and (n2%x==0)):
                       x=x-1
                       print(x)
                       break
                      
#num1=int(input("enter a number:"))
#num2=int(input("enter a number:"))
#print(a=gcd(num1,num2))

#a=gcd(num1,num2)  
#print(a)
 
