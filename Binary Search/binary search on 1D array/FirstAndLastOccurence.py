def firstandlastoccurence(nums,x):
    n=len(nums)

    low=0
    high=n-1
    first_occurence=-1
    second_occurence=-1
    while (low<=high):
        mid=(low+high)//2

        if x==nums[mid]:
            first_occurence=mid
            high=mid-1
        elif x<nums[mid]:
            high=mid-1
        else:
            low=mid+1

    low=0
    high=n-1

    while(low<=high):
        mid=(low+high)//2

        if x==nums[mid]:
            second_occurence=mid
            low=mid+1
        elif x<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    return first_occurence,second_occurence
        

print(firstandlastoccurence([5, 7, 7, 8, 8, 10],8))