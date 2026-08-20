def upperbound(nums,target):
    n=len(nums)

    low=0
    high=n-1
    ans=n

    while low<=high:
        mid=(low+high)//2

        if nums[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

print(upperbound([1, 2, 4, 4, 5, 7],3))

# Time :- O(log n)
# Space :- O(1)