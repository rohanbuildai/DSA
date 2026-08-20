# def splitarray_largestsum(nums,k):
#     n=len(nums)

#     low=max(nums)
#     high=sum(nums)
#     ans=0

#     while (low<=high):
#         mid=(low+high)//2

#         if countSubarrays(nums,mid) <= k:
#             ans=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return ans
# def countSubarrays(nums,count):
#     n=len(nums)
#     subarray=1
#     currentSum=0

#     for i in range (n):

#         if currentSum + nums[i] <= count:
#             currentSum+=nums[i]
#         else:
#             subarray+=1
#             currentSum=nums[i]
#     return subarray

# print(splitarray_largestsum([3,5,3,4],5))







# def splitarray_largestsum(A,B,C):
#     n=len(C)

#     low=max(C)
#     high=sum(C)
#     ans=0

#     if A > n:
#         return max(C)

#     while (low<=high):
#         mid=(low+high)//2

#         if countSubarrays(C,mid) <= A:
#             ans=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return (ans * B) % 10000003 
# def countSubarrays(C,count):
#     n=len(C)
#     subarray=1
#     currentSum=0

#     for i in range (n):

#         if currentSum + C[i] <= count:
#             currentSum+=C[i]
#         else:
#             subarray+=1
#             currentSum=C[i]
#     return subarray

# print(splitarray_largestsum(10,1,[1, 8, 11, 3]))













def splitarray_largestsum(nums,k):
    n=len(nums)

    return countSubarrays(nums,k) 

def countSubarrays(nums,count):
    n=len(nums)
    subarray=1
    currentSum=0

    for i in range (n):

        if currentSum + nums[i] <= count:
            currentSum+=nums[i]
        else:
            subarray+=1
            currentSum=nums[i]
    return subarray

print(splitarray_largestsum([1,2],3))