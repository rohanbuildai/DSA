def maximumconsecutiveones(nums):

    count=0
    max_count=0
    for num in nums:
        if num==1:
            count+=1
            max_count=max(max_count,count)
        else:
            count=0
    return max_count


print(maximumconsecutiveones([1,33,1,1,1,3,3,4,1,1,1,1,1,1]))