# brute force :- 
# time  :- O((sum(nums) - max(nums) × N))

# def bookallocation(nums,m):

#     minimum_pages = max(nums)
#     maxinum_pages = sum(nums)

#     for pages in range ( minimum_pages , maxinum_pages + 1 ) :
#         if countStudents ( nums , pages ) <= m :
#             return pages

# def countStudents ( nums , pages ) :
#     n = len ( nums )
#     student = 1
#     allotedPages = 0

#     for i in range ( n ) :
#         if allotedPages + nums[i] <= pages :
#             allotedPages += nums[i]
#         else:
#             student += 1
#             allotedPages = nums[i]
#     return student


# print ( bookallocation ( [ 12, 34, 67, 90 ] , 2) )




# optimal solution :-
# time :- 

# def bookallocation( nums , m ) :

#     low = max ( nums )
#     high = sum ( nums )
#     ans = 0

#     if m > len(nums) :
#         return -1

#     while ( low <= high ) :
#         mid = ( low + high ) // 2

#         if countStudents ( nums , mid ) <= m:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans

# def countStudents ( nums , pages ) :
#     n = len ( nums )
#     student = 1
#     allotedPages = 0

#     for i in range ( n ) :
#         if allotedPages + nums[i] <= pages :
#             allotedPages += nums[i]
#         else:
#             student += 1
#             allotedPages = nums[i]
#     return student


# print ( bookallocation ( [ 12, 34, 67, 90 ] , 2 ) )





# def bookallocation( nums , m ) :

#     low = max ( nums )
#     high = sum ( nums )
#     ans = 0

#     while ( low <= high ) :
#         mid = ( low + high ) // 2

#         if countSubarrays ( nums , mid ) <= m:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans
    

# def countSubarrays ( nums , count ) :
#     n = len ( nums )
#     subarray = 1
#     currentElement = 0

#     for i in range ( n ) :
#         if currentElement + nums[i] <= count :
#             currentElement += nums[i]
#         else:
#             subarray += 1
#             currentElement = nums[i]
#     return subarray


# print ( bookallocation ( [ 1,2,3,4,5 ] , 2 ) )




