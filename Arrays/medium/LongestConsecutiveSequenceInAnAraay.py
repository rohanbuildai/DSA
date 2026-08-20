def longestconsecutivesequenceinanarray(nums):
    n=len(nums)

    longest=0

    numset=set(nums)

    for num in numset:
        if num-1 not in numset:
            current_element=num
            highest=1

            while current_element+1 in numset:
                current_element+=1
                highest+=1
            longest=max(longest,highest)
    return longest

print(longestconsecutivesequenceinanarray([100,4,200,1,3,2]))