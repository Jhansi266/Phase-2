def performinsertionsort(nums):
    n=len(nums)
    lasteleinsortedarr=0
    for firstindex in range(1,n):
        temp=nums[firstindex]
        previous=lasteleinsortedarr
        while previous>=0 and nums[previous]>temp:
            nums[previous+1]=nums[previous]
            previous-=1
        nums[previous+1]=temp
        lasteleinsortedarr+=1
nums=[10,3,23,67,8]
print("before sorting",nums)
performinsertionsort(nums)
print("after sorting",nums)
