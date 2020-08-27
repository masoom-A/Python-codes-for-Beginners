def digit_pair(n):
    for x in n:
        final_list=[]
        if x<=500 and x>=10:
            list1=[]
            list2=[]
            for y in str(x):
                list1.append(y)
            a=max(list1)
            b=min(list1)
            c=a*11+b*7
            if c>99:
               for z in str(c):
                   list2.append(z)
               final_list=list2[1]+list2[2]
            
            else:
                
                return final_list.append(c)
        else:
            return final_list
            
length=int(input("enter the length of the input"))
n=[]
                 
                 
for x in range (1,length):
    n.append(x)
    
print(digit_pair(n))
    
    
