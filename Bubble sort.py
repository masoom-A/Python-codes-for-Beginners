#Bubble sort
def bubble(nums):
    for i in range(0,len(nums)-1,1):
                    
        for j in range(len(nums)-1):
                        
            if nums[j]>nums[j+1]:
                            
                (nums[j],nums[j+1])=(nums[j+1],nums[j])
                           
               
n=int(input())

nums=[]
for x in range(n):
    ele=int (input())
    nums.append(ele)
    
bubble(nums)
print(nums)

