def insert(list):
    for start in range(len(list)):
        pos=start
        while pos>0 and list[pos]<list[pos-1]:
            (list[pos],list[pos-1])=(list[pos-1],list[pos])
            pos=pos-1
#list=[2,4,1,3,5]
list=list(range(-500,0,1))
insert(list)
print(list)
