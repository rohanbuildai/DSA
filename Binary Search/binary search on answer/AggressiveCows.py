#brute force :-
#Time :- O(nlogn+n×(maxPosition−minPosition))

# def aggressivecows(nums,k):
#     nums.sort()

#     maximum = max(nums)
#     minimum = min(nums)

#     if k == 2:
#         return (maximum-minimum)

#     for i in range (1,((maximum - minimum) + 1)):
#         if canWePlace(nums,i,k) == True :
#             continue
#         else:
#             return i-1
        
# def canWePlace(nums,dist,cows):
#     n=len(nums)
#     countCows=1
#     lastCow=nums[0]

#     for i in range (1,n):
#         if nums[i] - lastCow >= dist :
#             countCows += 1
#             lastCow = nums[i]
#     if countCows >= cows :
#         return True
#     else:
#         return False

# print(aggressivecows( [4, 2, 1, 3, 6],2))



# optimal :-
# time :- O(nlogn+nlog(maxPosition−minPosition))

# def aggressivecows(nums,k):
#     nums.sort()
#     n=len(nums)

#     low = 1
#     high = nums[n-1] - nums[0]
#     ans=0

#     while (low <= high) :
#         mid = (low + high) // 2

#         if canWePlace(nums, mid, k) == True :
#             ans = mid
#             low = mid + 1
#         else:
#             high = mid - 1
#     return ans
        
# def canWePlace(nums,dist,cows):
#     n=len(nums)
#     countCows=1
#     lastCow=nums[0]

#     for i in range (1,n):
#         if nums[i] - lastCow >= dist :
#             countCows += 1
#             lastCow = nums[i]
#     if countCows >= cows :
#         return True
#     else:
#         return False

# print(aggressivecows( [0, 3, 4, 7, 10, 9],4))








def aggressive_cows(nums,k):
    nums.sort()

    low=min(nums)
    high=max(nums)

    while (low<=high):
        mid=(low+high) // 2

        if canweplace(nums,mid,k) == True :
            low=mid+1
        else:
            high=mid-1
    return high

def canweplace(nums,dist,cows):
    n=len(nums)

    countcows = 1
    lastcow = nums[0]

    for i in range (1,n) :

        difference = nums[i] - lastcow

        if difference >= dist :
            countcows+=1
            lastcow = nums[i]
    if countcows >= cows:
        return True
    else:
        return False



print(aggressive_cows( [0, 3, 4, 7, 10, 9],4))