# optimal approach :-
# time :- O(n log(max(nums)))

import math
def findthesmallestdivisior(nums,threshold):
    n=len(nums)
    max_number=max(nums)

    low=1
    high=max_number
    ans=float("inf")

    while low<=high:
        mid=(low+high)//2
        division_sum=0

        for i in range (n):
            division_sum+=math.ceil(nums[i]/mid)
        if division_sum <= threshold:
            ans=min(ans,mid)
            high=mid-1
        else:
            low=mid+1
    return ans

print(findthesmallestdivisior( [1,2,5,9],6))