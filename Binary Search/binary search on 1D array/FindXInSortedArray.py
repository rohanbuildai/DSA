def findxinsortedarray(nums,target):
    n=len(nums)
    low=0
    high=n-1
    

    while low<=high:
        mid=low+(high-low)//2

        if target > nums[mid]:
            low=mid+1
        elif target < nums[mid]:
            high=mid-1
        else:
            return mid
    return -1


print(findxinsortedarray([-1,0,3,5,9,12],9))

# Time :- O(log n)
# Space :- O(1)