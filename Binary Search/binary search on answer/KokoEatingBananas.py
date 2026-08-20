# brute force :-
# time :- O(max(arr) x n)    // will cause overflow


# def kokoeatingbananas(piles,h):
#     n=max(piles)

#     for i in range (1,n+1):
#         hour=0
#         for j in range (len(piles)):
#             hour+=math.ceil(piles[j]/i)
        
#         if hour <= h:
#             return i

# print(kokoeatingbananas([3,6,7,11],8))




#optimal approach :-
# time :- O(log n)

# def kokoeatingbananas(piles,h):
#     n=len(piles)
#     ans=float("inf")
#     low=1
#     high=max(piles)

#     while (low<=high):
#         mid=(low+high)//2
#         hour=0

#         for i in range (n):
#             hour += (piles[i] + mid - 1) // mid        # // math.ceil equivanlent
#         if hour<=h:
#             ans=min(ans,mid)
#             high=mid-1
#         else:
#             low=mid+1
#     return ans

# print(kokoeatingbananas([30,11,23,4,20],5))














import math
def kokoeatingbananas(piles,h):
    n=len(piles)

    low=1
    high=max(piles)

    while(low<=high):
        mid=(low+high)//2

        if countHours(piles,mid) <= h:
            high=mid-1
        else:
            low=mid+1
    return low

def countHours(piles,eatingSpeed):
    n=len(piles)
    hours=0

    for i in range (n):
        hours+=(piles[i] + eatingSpeed - 1) // eatingSpeed
    return hours


print(kokoeatingbananas([30],5))