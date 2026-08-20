def checkifarrayissorted(nums):
    n=len(nums)
    flag=0
    for i in range (0,n-1):
        if nums[i] > nums[i+1]:
            return False
        else:
            flag+=1

    if flag==len(nums)-1:
        return True
print(checkifarrayissorted([1,2,3,4,5]))