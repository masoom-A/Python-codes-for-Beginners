def insertion(a):
    for i in range (len(a)):
        pos=i
        while(pos>0 and a[pos]<a[pos-1]):
            (a[pos],a[pos-1])=(a[pos-1],a[pos])
            print(a)
            pos=pos-1
a=[3,2,5,4,1]
insertion(a)
    
