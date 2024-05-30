class linear:
    target=67
    flag=-1
    def list(self,nums):
        n=len(nums)
        target=67
        flag=-1
        for index in range(n):
            if nums[index]==target:
                flag=index
                break
        if flag==-1:
            print("not found")
        else:
            print("target is found",flag)
s=linear()
nums=[10,20,67,89]
s.list(nums)
