count=0
list1=[2,4,5,1,5]
for x in range(len(list1)):
    for y in range (1,len(list1)):
        if list1[x]==list1[y]:
            print(list1[x])
