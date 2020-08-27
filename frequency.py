str=""
for x in range (1,10):
    ele=input()
    str=str+ele
list=[]
for y in str:
    if y not in list:
        list.append(y)
        count=str.count(y)
        print("{} occurs {} times".format(y,count))
       

          
