def dict(value):
    b=[]
    for v in value.values():
        b.append(v)
    b.sort()
    for x in range (0,len(b)):
        print(b[x])
values= {0: 10, 1: 20}
values[3]=30
values[4]=40
values[5]=50:

dict(values)
    
