# Better Solution :- 
# Time Complexity :- O(n^2)
# Space Complexity :- O(n)


# def threesum(arr):
#     n=len(arr)
#     result = set()

#     for i in range (n):
#         hashmap = set()
#         for j in range (i+1,n):
#             Sum=-(arr[i]+arr[j])

#             if Sum in hashmap:
#                 triplet=tuple(sorted((arr[i],arr[j],Sum)))
#                 result.add(triplet)
#             hashmap.add(arr[j])
#     return result


# print(threesum([2,-2,0,3,-3,5]))



# Optimal Solution :- 
# Time Complexity :- O(n^2)
# Space Complexity :- O(1)



def threesum(arr):
    n=len(arr)
    arr.sort()
    ans=[]
    i=0

  

    while i<n-2:
        if i > 0 and arr[i]==arr[i-1]:
            i+=1
            continue
        j=i+1
        k=n-1
        while j<k:
            current_sum=arr[i]+arr[j]+arr[k]

            if current_sum<0:
                j+=1
            elif current_sum>0:
                k-=1
            else:
                ans.append([arr[i],arr[j],arr[k]])
                j+=1
                k-=1
                while j < k and arr[j] == arr[j-1]:
                    j+=1
                while j < k and arr[k] == arr[k+1]:
                    k-=1
        i+=1
    return ans


print(threesum([2,-2,0,3,-3,5]))
