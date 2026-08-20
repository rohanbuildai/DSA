# brute force :-
# time :- O(mini-maxi x n)


# def minimumnumberofdaysrequiredtomakeMbouquets(bloomDay, m, k):
#     n=len(bloomDay)
#     minimumPossibleDay=min(bloomDay)
#     maximumPossibleDay=max(bloomDay)

#     if m*k > n:
#         return -1
   

#     for days in range (minimumPossibleDay,maximumPossibleDay+1):
#         count=0
#         bouquets=0
#         for i in range (n):
#             if bloomDay[i] <= days:
#                 count+=1
#             else:
#                 bouquets+=count//k
#                 count=0
#         bouquets+=count//k

#         if bouquets>=m:
#             return days

# print(minimumnumberofdaysrequiredtomakeMbouquets([7,7,7,7,13,11,12,7],2,3))




# optimal solutuion :- 
# time :- O(n × log(maxDay - minDay))



def minimumnumberofdaysrequiredtomakeMbouquets(bloomDay, m, k):
    n=len(bloomDay)
    ans=0

    low=min(bloomDay)
    high=max(bloomDay)

    if m*k > n:
        return -1

    while (low<=high):
        count=0
        bouquets=0
        mid=(low+high)//2

        for i in range (n):
            if bloomDay[i] <= mid:
                count+=1
            else:
                bouquets+=count//k
                count=0
        bouquets+=count//k

        if bouquets >= m:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

print(minimumnumberofdaysrequiredtomakeMbouquets([7,7,7,7,13,11,12,7],2,3))



















def minimumnoofdaysrequiredtomakembouquets(flowers,m,k):
    n=len(flowers)

    low=min(flowers)
    high=max(flowers)

    if m * k > n:
        return -1

    while (low<=high):
        mid=(low+high)//2

        if countBouquets(flowers,mid,k) >= m:
            high=mid-1
        else:
            low=mid+1
    return low

def countBouquets(flowers,bloomday,noOfBouquets):
    n=len(flowers)
    countOfBouquets=0
    countFlowers=0

    for i in range (n):
        if flowers[i]<=bloomday:
            countFlowers+=1
        else:
            countOfBouquets+=countFlowers//noOfBouquets
            countFlowers=0
    countOfBouquets+=countFlowers//noOfBouquets
    return countOfBouquets

print(minimumnoofdaysrequiredtomakembouquets([7,7,7,7,12,11,7],2,3))