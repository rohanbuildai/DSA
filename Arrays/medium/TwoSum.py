#optimal approach only if array is sorted or i am allowed to sort

# def twosum(arr,target):
    
#     n=len(arr)

#     sorted(arr)

#     i=0
#     j=n-1
#     while (i<j):
#         if (arr[i]+arr[j]>target):
#             j-=1
#         elif (arr[i]+arr[j]<target):
#             i+=1
#         else:
#             return arr[i],arr[j]


# print(twosum([1, 6, 2, 10, 3],4))



#better one if i am not allowed to sort or array is not sorted :- use hashmap

def twosum(arr,target):

    n=len(arr)
    hashmap={}

    for i in range (n):
        more=target-arr[i]

        if more in hashmap:
            return hashmap[more],i
        hashmap[arr[i]]=i





print(twosum([1, 6, 2, 10, 3],4))