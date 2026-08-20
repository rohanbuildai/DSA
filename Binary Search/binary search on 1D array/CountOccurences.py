def countoccurences(nums,x):
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
    if first_occurence==-1:
        return 0
    return (second_occurence-first_occurence)+1
        

print(countoccurences(  [2,4,4,4,6,8],4))