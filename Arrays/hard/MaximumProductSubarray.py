def maximumproductsubarray(nums):
    n=len(nums)

    suffix=1
    prefix=1
    ans=float("-inf")

    for i in range (n):
        if prefix==0:
            prefix=1
        if suffix==0:
            suffix=1
        prefix*=nums[i]
        suffix*=nums[n-1-i]

        ans=max(ans,max(prefix,suffix))

    return ans



print(maximumproductsubarray([-2,3,4,-1,0,-2,3,1,4,0,4,6,-1,4]))

# Time :- O(n)
# Space :- O(1)