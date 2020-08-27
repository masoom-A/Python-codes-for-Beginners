#test bubble
def bubble(list):
    for i in range (len(list)):
         for j in range(len(list)):
             if list[i]<list[j]:
                (list[i],list[j])=(list[j],list[i])
list=[1,5,3,2,4]
bubble(list)
print(list)
