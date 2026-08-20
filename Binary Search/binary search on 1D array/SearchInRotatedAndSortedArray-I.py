def searchinroatedsortedarray_I(nums,k):
    n=len(nums)

    low=0
    high=n-1

    while (low<=high):
        mid=(low+high)//2

        if nums[mid]==k:
            return mid
        if nums[low]<=nums[mid]:
            if nums[low]<=k<nums[mid]:
              high=mid-1
            else:
              low=mid+1
        else:
            if nums[mid]<k<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
print(searchinroatedsortedarray_I([4, 5, 6, 7, 0, 1, 2],2))