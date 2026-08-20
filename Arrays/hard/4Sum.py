# Better Solution :- 
# Time Complexity :- O(n^3)
# Space Complexity :- O(n)



# def foursum(nums,target):
#     n=len(nums)
#     res=set()

#     for i in range (n):
#         hashmap=set()
#         for j in range (i+1,n):
#             for k in range (j+1,n):
#                 fourth=target-nums[i]-nums[j]-nums[k]

#                 if fourth in hashmap:
#                     quadriplet=tuple(sorted((nums[i],nums[j],nums[k],fourth)))
#                     res.add(quadriplet)
#                 hashmap.add(nums[k])
#     return res

# print(foursum( [1, -2, 3, 5, 7, 9],7))




# optimal Solution :- 
# Time Complexity :- O(n^3)
# Space Complexity :- O(1)



def foursum(nums,target):
    n=len(nums)
    nums.sort()
    result=[]

    for i in range (n-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range (i+1,n-2):
            if j > i+1 and nums[j]==nums[j-1]:
                continue
            k=j+1
            l=n-1

            while k<l:


                current_sum=nums[i]+nums[j]+nums[k]+nums[l]

                if current_sum < target:
                    k+=1
                elif current_sum > target:
                    l-=1
                else:
                    result.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1

                    while k<l and nums[k] == nums[k-1]:
                        k+=1
                    while k<l and nums[l] == nums[l+1]:
                        l-=1
    return result
print(foursum([1,0,-1,0,-2,2],0))