# Optimal Approach :-
# Time Complexity :- O(n)
# Space Complexity :- O(n)
def largestsubarraywithsum0(nums):
    n=len(nums)
    maxlength=0
    hasharray={0:-1}
    Sum=0

    for i in range (n):
        Sum+=nums[i]

        if Sum in hasharray:
            length=i-hasharray[Sum]
            maxlength=max(maxlength,length)
        else:
            hasharray[Sum]=i
    return maxlength



print(largestsubarraywithsum0( [1,2,3,1,1,1,1]))