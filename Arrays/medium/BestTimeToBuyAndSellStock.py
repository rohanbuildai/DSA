# def besttimetobuyandsellstock(arr):
#     n=len(arr)

#     buy=arr[0]
#     profit=0

#     for i in range (1,n):
#         cost=arr[i]-buy
#         profit=max(profit,cost)

#         buy=min(buy,arr[i])
#     return profit    


# print(besttimetobuyandsellstock([10,7,5,8,11,9]))



def besttimetobuyandsellstock(arr):
    n=len(arr)
    max_profit=0
    buy=arr[0]

    for i in range (1,n):
        profit=arr[i]-buy
        max_profit=max(max_profit,profit)

        buy=min(buy,arr[i])
    return max_profit

print(besttimetobuyandsellstock([10,7,5,8,11,9]))