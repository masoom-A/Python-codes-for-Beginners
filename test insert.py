def insert(list):
    
    for i in range(1,len(list)):
        current_value=list[i]
        while current_value<list[i-1] and i>0:
            (list[i],list[i-1])=(list[i-1],list[i])
            i=i-1

            
list=[5,2,4,1,3]
insert(list)
print(list)
