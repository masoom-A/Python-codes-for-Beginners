num=int(input("enter a number:"))
for x in range(2,num):
    if num%x==0:
        print("number is not prime:")
        break
else:
    print("number is prime")
        
  
