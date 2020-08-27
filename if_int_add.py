n1=input()
n2=input()
if not isinstance(n1,int) and isinstance(n2,int):
    raise TypeError("input must be int")
else:
    n3=int(n1)+int(n2)
    print(n3)

    
