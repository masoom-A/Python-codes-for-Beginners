##selection sort
def select(l):
    for i in range(len(l)):
        minpos=i
        for j in range(i,len(l)):
            if l[j]<l[minpos]:
                minpos=j
        (l[i],l[minpos])=(l[minpos],l[i])
##        temp=l[i]
##        l[i]=l[minpos]
##        l[minpos]=temp
l=[1,5,4,2,3]
select(l)
print(l)

