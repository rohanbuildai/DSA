# def mergetwosortedarrayswithoutusingextraspace(nums1,m,nums2,n):

#     i=0
#     j=0

#     while i<m and j<n:
#         if nums1[i]<nums2[j]:
#             i+=1
#         else:
#             nums1[i],nums2[j]=nums2[j],nums1[i]
#             k=0

#             while k < n-1 and nums2[k] > nums2[k+1]:
#                 nums2[k] , nums2[k+1] = nums2[k+1] , nums2[k]
#                 k+=1
#             i+=1
#     return nums1,nums2


# print(mergetwosortedarrayswithoutusingextraspace([-5, -2, 4, 5], 4 ,[-3, 1, 8], 3 ))


# Optimal Approach :-
# Space :- O(1)
# Time :- O(m+n)

def mergetwosortedarrayswithoutusingextraspace(nums1,m,nums2,n):

    i=m-1
    j=n-1
    k=m+n-1

    while i>=0 and j>=0:
        
        if nums2[j]>nums1[i]:
            nums1[k]=nums2[j]
            k-=1
            j-=1
        else:
            nums1[k]=nums1[i]
            i-=1
            k-=1
    while j>=0:
        nums1[k]=nums2[j]
        k-=1
        j-=1
    return nums1


print(mergetwosortedarrayswithoutusingextraspace([1,2,3,0,0,0], 3 ,[2,5,6], 3 ))