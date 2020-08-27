year=int(input("enter the year: "))
if (year%100==0)and (year%400==0):
    print("this is a leap year")
else:
    if(year%100!=0)and(year%4==0):
        print("this is a leap year")
    else:
        print("this is not a leap year")
        
    
    
