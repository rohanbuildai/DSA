def kadanesalgorithm(nums):
    n=len(nums)

    sum=0
    Max=float('-inf')

    for i in range(n):
        sum+=nums[i]
        Max=max(Max,sum)

        if sum<0:
            sum=0

    return Max


print(kadanesalgorithm([-2,-3,-7,-2,-10,-4]))