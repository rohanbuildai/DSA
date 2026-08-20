# def subarraysumequalsk(nums,k):
#     n=len(nums)
#     current_sum=0
#     hash_map={0:1}
#     count=0

#     for i in range (n):
#         current_sum+=nums[i]
#         more=current_sum-k

#         if more in hash_map:
#             count+=hash_map[more]
#         if current_sum in hash_map:
#             hash_map[current_sum] += 1
#         else:
#             hash_map[current_sum] = 1

#     return count


def sabarraysumequalsk(arr,k):
    n=len(arr)

    prefix_sum=0
    hash_map={0:1}
    count=0

    for i in range (n):
        prefix_sum+=arr[i]
        more=prefix_sum-k

        if more in hash_map:
            count+=hash_map[more]
        if prefix_sum in hash_map:
            hash_map[prefix_sum]+=1
        else:
            hash_map[prefix_sum]=1
    return count

print(sabarraysumequalsk([1,2,3],3))