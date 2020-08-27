list1=[10,10,20,30,20,40,30,40]
pair=0
for x in list1:
    pair=pair+(list1.count(x)//2)
print(pair)
###########################################
count1=0
    sum=0
    templist=[]
    final_list=[]
    for x in ar:
        if x not in templist:
            templist.append(x)
    for y in templist:
        final_list.append(ar.count(y))   
    for pair in final_list:
        sum=sum+(pair//2)      
        
    return sum
