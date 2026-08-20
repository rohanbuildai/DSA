#brute force :-
# time :- O(n × (sum(weights) - max(weights)))

# def capacity_to_ship_packages_within_d_days(weights,days):
#     n=len(weights)

    # minimum_capacity=max(weights)
    # maximum_capacity=sum(weights)

    # for i in range (minimum_capacity,maximum_capacity+1):
    #     days_used=1
    #     load_capacity=0
    #     for j in range(n):
    #         if load_capacity+weights[j] > i:
    #             days_used+=1
    #             load_capacity=weights[j]
    #         else:
    #             load_capacity+=weights[j]
    #     if days_used <= days :
    #         return i

# optimal solution :-
# time:- O(n × log(sum(weights)))
#     n=len(weights)
#     low=max(weights)
#     high=sum(weights)
#     ans=0

#     while (low<=high):
#         mid=(low+high)//2
#         load=0
#         day=1

#         for i in range (n):
#             if load+weights[i] > mid:
#                 day+=1
#                 load=weights[i]
#             else:
#                 load+=weights[i]
#         if day <= days:
#             ans=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return ans

# print(capacity_to_ship_packages_within_d_days([1,2,3,4,5,6,7,8,9,10],5))



















def capacitytoshippackageswithinddays(weights,days):
    n=len(weights)

    low = max(weights)
    high = sum(weights)

    while (low<=high):
        mid=(low+high) // 2

        if daysRequired(weights,mid) <= days:
            high=mid-1
        else:
            low=mid+1
    return low

def daysRequired(weights,capacity):
    n=len(weights)
    load=0
    days_required=1

    for i in range (n):
        if load+weights[i] <= capacity:
            load+=weights[i]
        else:
            days_required+=1
            load=weights[i]
    return days_required


print(capacitytoshippackageswithinddays([3,2,2,4,1,4],3))