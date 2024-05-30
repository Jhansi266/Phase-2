def bubble(nums):
    n=len(nums)
    fixindex=n-1
    while fixindex>0:
       for i in range(n-1):
        
        if nums[i]>nums[i+1]:
            temp=nums[i]
            nums[i]=nums[i+1]
            nums[i+1]=temp
    print(nums)
    i-=1


nums=[10,3,8,56,89,2]
print("before sorting",nums)
bubble(nums)
print("after sorting",nums)
