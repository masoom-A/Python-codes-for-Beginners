#quick sort
def pivot_place(list1,first,last):
    pivot=list1[first]
    left=first+1
    right=last
    while True:
        while left<=last and list1[left]<=list1[right]:
            left=left+1
        while left<=right and list1[right]>=list1[left]:
            right=right-1
        if right<left:
            break
           
        else:
             (list1[left],list1[right])=(list1[right],list1[left])
             
    (list1[first],list1[right])=(list1[right],list1[first])
    
    return right #correct position of pivot

def quick_sort(list1,first,last):
    if first<last:
        p=pivot_place(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
    
    
        
        
    



#list1=[56,26,93,17,31,44]
list1=[int(input()) for x in range(5)]           
n=len(list1)-1
quick_sort(list1,0,n)
print(list1)
