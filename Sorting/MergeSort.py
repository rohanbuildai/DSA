# def Merge_Sort(arr,low,high):
#     n=len(arr)

#     if low>=high:
#         return 
#     mid=(low+high)//2
#     Merge_Sort(arr,low,mid)
#     Merge_Sort(arr,mid+1,high)
#     Merge(arr,low,mid,high)

#     return arr

# def Merge(arr,low,mid,high):
#     result=[]

#     left=low
#     right=mid+1

#     while(left<=mid and right<=high):
#         if (arr[left]<=arr[right]):
#             result.append(arr[left])
#             left+=1
#         else:
#             result.append(arr[right])
#             right+=1
#     while(left<=mid):
#         result.append(arr[left])
#         left+=1
#     while(right<=high):
#         result.append(arr[right])
#         right+=1

#     for i in range ((len(result))):
#         arr[low+i]=result[i]


# print(Merge_Sort([3,2,4,1,3],0,4))



# def mergesort(arr,low,high):
#     n=len(arr)

#     if low>=high:
#         return

#     mid=(low+high)//2

    
#     mergesort(arr,low,mid)
#     mergesort(arr,mid+1,high)
#     merge(arr,low,mid,high)

#     return arr


# def merge(arr,low,mid,high):

#     result=[]
#     left=low
#     right=mid+1

#     while(left<=mid and right<=high):
#         if (arr[left]<=arr[right]):
#             result.append(arr[left])
#             left+=1
#         else:
#             result.append(arr[right])
#             right+=1
#     while (left<=mid):
#         result.append(arr[left])
#         left+=1
#     while(right<=high):
#         result.append(arr[right])
#         right+=1
#     for i in range (len(result)):
#         arr[low+i]=result[i]

# print(mergesort([3,2,4,1,3],0,4))




# def mergesort(arr,low,high):
#     n=len(arr)

#     if low >=high:
#         return

#     mid=(low+high)//2

#     mergesort(arr,low,mid)
#     mergesort(arr,mid+1,high)
#     merge(arr,low,mid,high)

#     return arr


# def merge(arr,low,mid,high):
#     result=[]
#     left=low
#     right=mid+1

#     while (left<=mid and right<=high):
#         if arr[left]<=arr[right]:
#             result.append(arr[left])
#             left+=1
#         else:
#             result.append(arr[right])
#             right+=1
#     while left<=mid:
#         result.append(arr[left])
#         left+=1
#     while right<=high:
#         result.append(arr[right])
#         right+=1
#     for i in range (len(result)):
#         arr[low+i]=result[i]

# print(mergesort([3,2,4,1,3],0,4))



