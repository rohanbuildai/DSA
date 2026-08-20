# Brute Force :- 
# time :- O(k * n)
# space :- O(n)

# def minimisemaxdistancetogasstation(arr,k):
#     n=len(arr)
#     how_many = [0]*(n-1)

#     for _ in range (1,k+1):
#         max_value = -1
#         max_index = -1

#         for i in range (n-1):
#             difference = arr[i+1] - arr[i]
#             section_length = difference / (how_many[i]+1)

#             if max_value < section_length:
#                 max_value=section_length
#                 max_index=i

#         how_many[max_index]+=1
#     ans=-1

#     for i in range (n-1):
#         difference = arr[i+1] - arr[i]
#         section_length = difference / (how_many[i] + 1)

#         ans=max(ans,section_length)
#     return ans

# print(minimisemaxdistancetogasstation([1,13,17,23],5))




# better solution :- 
# time :- O((n + k) log n)
# space :- O(n)


# import heapq

# def minimisemaxdistancetogasstation(arr,k):
#     n=len(arr)
#     how_many = [0]*(n-1)
#     heap = []

#     for i in range (n-1):
#         heapq.heappush(heap,(-(arr[i+1]-arr[i]),i))

#     for _ in range (1,k+1):
#         value , index = heapq.heappop(heap)
#         value=-value
#         how_many[index]+=1
#         initial_difference=arr[index+1] - arr[index]
#         new_section_length = initial_difference / (how_many[index]+1)
#         heapq.heappush(heap,(-new_section_length,index))


#     return -heap[0][0]

# print(minimisemaxdistancetogasstation([1,13,17,23],5))











def minimisemaxdistancetogasstation(arr,k):
    n=len(arr)
    howMany=[0]*(n-1)

    for _ in range (1,k+1):
        max_length = -1
        max_index = -1

        for i in range (n-1):
            difference = arr[i+1] - arr[i]
            section_length = difference / (howMany[i]+1)

            if max_length < section_length :
                max_length = section_length
                max_index = i
        howMany[max_index] += 1
    ans = -1

    for i in range (n-1):
        difference = arr[i+1] - arr[i]
        section_length = difference / (howMany[i]+1)

        ans = max(ans,section_length)

    return ans



print(minimisemaxdistancetogasstation([1,13,17,23],5))