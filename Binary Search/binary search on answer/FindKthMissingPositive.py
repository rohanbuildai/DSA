# brute force :- 
# time :- O(n)


# def findkthmissingpositive(nums,k):
#     n=len(nums)
    
#     for i in range (n):
#         if nums[i] <= k:
#             k+=1
#         else:
#             return k

# print(findkthmissingpositive( [1, 4, 6, 8, 9],3))




#optimal solution :-
# time :- O(log n)

def findkthmissingpositive(nums,k):
    n=len(nums)
    low=0
    high=n-1

    while (low<=high):
        mid=(low+high)//2
        missing=nums[mid] - (mid+1)

        if missing < k:
            low=mid+1
        else:
            high=mid-1
    return low+k

print(findkthmissingpositive( [1, 4, 6, 8, 9],3))