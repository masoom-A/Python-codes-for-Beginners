#insertion sort:let firsr element is sorted and rest are unsorted.
def insert(nums):
    for i in range (1,len(nums)):
        current_ele=nums[i]
        pos=i
        while current_ele<nums[pos-1] and pos>0:
            #nums[i]=nums[i-1]
            (nums[pos],nums[pos-1])=(nums[pos-1],nums[pos])
            pos=pos-1
        #nums[i]=current_ele
 
nums=[5,2,4,1,3]
insert(nums)
print(nums)
