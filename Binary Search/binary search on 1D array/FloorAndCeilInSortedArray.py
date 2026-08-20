def floorandceilinsortedarray(nums,x):
    n=len(nums)

    floor=-1
    ceil=-1
    low=0
    high=n-1
    mid=(low+high)//2

    while (low<=high):
        mid=(low+high)//2

        if nums[mid]<=x:
            floor=nums[mid]
            low=mid+1
        else:
            high=mid-1

    low=0
    high=n-1

    while (low<=high):
        mid=(low+high)//2

        if nums[mid]>=x:
            ceil=nums[mid]
            high=mid-1
        else:
            low=mid+1
    
    return floor,ceil

print(floorandceilinsortedarray( [3, 4, 4, 7, 8, 10],4))

# Time :- O(log n)
# Space :- O(1)