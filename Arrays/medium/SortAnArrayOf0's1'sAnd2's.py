#brute force solution

# def sortanarrayof0_1and2(nums):

#     n=len(nums)
#     count_0=0
#     count_1=0
#     count_2=0

#     for i in range (0,n):
#         if nums[i]==0:
#             count_0+=1
#         elif nums[i]==1:
#             count_1+=1
#         else:
#             count_2+=1
#     for i in range (count_0):
#         nums[i]=0
#     for j in range (count_0,count_1+count_0):
#         nums[j]=1
#     for k in range (count_1+count_0,n):
#         nums[k]=2

#     return nums



# print(sortanarrayof0_1and2([2,1,0,2,1,0]))

# the optimal solution:-


# def sortanarrayof0_1and2(nums):

#     n=len(nums)

#     low=0
#     mid=0
#     high=len(nums)-1

#     while mid<=high:
#         if nums[mid]==0:
#             nums[low],nums[mid]=nums[mid],nums[low]
#             low+=1
#             mid+=1
#         elif nums[mid]==1:
#             mid+=1
#         else:
#             nums[mid],nums[high]=nums[high],nums[mid]
#             high-=1
#     return nums


# print(sortanarrayof0_1and2([0,1,1,0,1,2,1,2,0,0,0]))




def sortzerooneamndtwo(arr):

    n=len(arr)
    low=0
    mid=0
    high=n-1

    while (mid<=high):
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr


print(sortzerooneamndtwo([0,1,1,0,1,2,1,2,0,0,0]))