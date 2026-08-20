# def findsmallestpositive(arr):
#     n=len(arr)

#     i=0

#     while(i<n):
#         if arr[i]>=1 and arr[i]<=n and arr[i]!=arr[arr[i]-1]:
#             correct=arr[i]-1
#             arr[i],arr[correct]=arr[arr[i]-1],arr[i]
#         else:
#             i+=1
#     for i in range (n):
#         if arr[i]!=i+1:
#             return i+1
#     return n+1
    
        

# print(findsmallestpositive([3,4,-1,1]))

# def findsmallestpositive(arr):
#     n=len(arr)

#     for i in range (n):
#         if arr[i]>=1 and arr[i]<=n and arr[i]!=arr[arr[i]-1]:
#             correct=arr[i]-1
#             arr[i],arr[correct]=arr[correct],arr[i]
#     for i in range (n):
#         if arr[i]!=i+1:
#             return i+1,arr
#     return n+1

# print(findsmallestpositive([3,4,-1,1]))




def firstmissingsmallestpositive(nums):
    n=len(nums)

    for i in range (n):
        while nums[i]>=1 and nums[i]<=n and nums[i]!=nums[nums[i]-1]:
            correct=nums[i]-1
            nums[i],nums[correct]=nums[correct],nums[i]
    for i in range (n):
        if nums[i]!=i+1:
            return i+1
    return n+1


print(firstmissingsmallestpositive([3,4,-1,1]))