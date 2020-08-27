def list(nums):
    count=0
    for num in nums:
        if num==4:
           count=count+1
    return count        
print(list([1,4,3,5,4]))
print(list([4,5,4,6,4,3]))
