# same as lower bound problem no changes
def searchinsertposition(nums,target):
    n=len(nums)

    low=0
    high=n-1
    ans=n

    while low<=high:
        mid=(low+high)//2

        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

print(searchinsertposition([1, 3,5,6],2))

# Time :- O(log n)
# Space :- O(1)