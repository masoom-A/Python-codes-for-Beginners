def selectsort(l):
    for start in range (len(l)):
        minpos=start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos=i
        ##(l[start],l[minpos])=(l[minpos],l[start])
        temp=l[start]
        l[start]=l[minpos]
        l[minpos]=temp
l=[2,4,3,1,5]
selectsort(l)
print(l)


            

