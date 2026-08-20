def singlenumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result
print(singlenumber([3,1,2,4,3,1,4]))