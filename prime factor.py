num=int(input("enter a number:"))
d=2
while num>1:
    if num%d==0:
        print(d)
        num=num/d
    else:
        d=d+1
        continue
