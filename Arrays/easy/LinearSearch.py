def linearsearch(nums,target):
    n=len(nums)

    for i in range (n):
        if nums[i]==target:
            return i
        else:
            return -1
        

print(linearsearch([3,5,3,5,67,7,5,4,34,3],4554))