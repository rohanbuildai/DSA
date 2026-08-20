# def medianoftwosortedarrays(nums1,nums2):
#     m=len(nums1)
#     n=len(nums2)

#     i=0
#     j=0

#     merged_array=[]         # [1,2,3,4]

#     while i<m and j<n :
#         if nums1[i]<nums2[j]:
#             merged_array.append(nums1[i])
#             i+=1
#         else:
#             merged_array.append(nums2[j])
#             j+=1
#     while i<m:
#         merged_array.append(nums1[i])
#         i+=1
#     while j<n:
#         merged_array.append(nums2[j])
#         j+=1


#     x=len(merged_array)

#     if x % 2 == 0:
#         sum_of_median = merged_array[x//2] + merged_array[(x//2)-1]
#         median = sum_of_median / 2
#         return median
#     else:
#         return merged_array[x//2]

# print(medianoftwosortedarrays([1,2],[3,4]))



def medianoftwosortedarrays(nums1,nums2):

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m=len(nums1)
    n=len(nums2)

    left_side_should_contribute = ( ( m + n ) + 1 ) // 2

    low = 0
    high = m

    while ( low <= high ) :

        cut_1 = ( low + high ) // 2                              
        cut_2 = left_side_should_contribute - cut_1              

        l1 = float("-inf") if cut_1 == 0 else nums1[cut_1 - 1]
        r1 = float("inf") if cut_1 == m else nums1[cut_1]

        l2 = float("-inf") if cut_2 == 0 else nums2[cut_2 - 1]
        r2 = float("inf") if cut_2 == n else nums2[cut_2]

        if l1 <= r2 and l2 <= r1 :

            if ( m + n ) % 2 == 0 :
                return ( ( max ( l1 , l2 ) + min ( r1 , r2 ) ) / 2 )
            else:
                return max ( l1 , l2 )
            
        elif l1 > r2 :
            high = cut_1 - 1
        else:
            low = cut_1 + 1



print(medianoftwosortedarrays([1,3,8,9,15],[7,11,18,19,21,25]))