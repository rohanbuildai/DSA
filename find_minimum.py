def find_minimum(nums) :
    n=len(nums)
    largest = nums[0]
    second_largest = -1

    for i in range (1,n) :
        if nums[i] > largest :
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest and nums[i] != largest :
            second_largest = nums[i]
    return second_largest


print(find_minimum([2,17,1,4,8,12,7]))