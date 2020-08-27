def select(property,l):
    sublist=[]
    for x in l:
        if property(x):
            sublist.append(x)
    return (sublist)
l=[7,3,5,2,1,5]
select(property(),l)
print(sublist)
