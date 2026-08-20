#majority elements-I :-
#better solution
#time complexity :- O(n)
#space complexity :- O(n)



# def majorityelements_1(nums):
#     n=len(nums)

#     hasharray={}

#     for num in nums:
#         if num in hasharray:
#             hasharray[num]+=1
#         else:
#             hasharray[num]=1
#     for i in hasharray:
#         if hasharray[i]>(n/2):
#             return i
# print(majorityelements_1([1, 2, 1, 1, 3, 2,2]))



#majority element-I :-
#optimal solution :-
#time complexity :- O(n)
#space complexity :- O(1)



def majorityelement1(nums):
    n=len(nums)

    element=0
    count=0
    final_count=0

    for i in range (n):

        if count==0:
            element=nums[i]
            count=1
        elif element==nums[i]:
            count+=1
        else:
            count-=1
    for i in range (n):
        if nums[i]==element:
            final_count+=1
    if final_count>n//2:
        return  element
    else:
        return None


print(majorityelement1([7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]))




#majority elements-II
# Better Solution :-
# Time Complexity :- O(n)
# Space Complexity :- O(n)



# def majorityelements_2(nums):
#     result=[]
#     n=len(nums)

#     hasharray={}

#     for num in nums:
#         if num in hasharray:
#             hasharray[num]+=1
#         else:
#             hasharray[num]=1
#     for i in hasharray:
#         if hasharray[i]>(n/3):
#             result.append(i)
#     return result
# print(majorityelements_2([1, 2, 1, 1, 3, 2,2]))



#majority elements-II
# optimal Solution :-
# Time Complexity :- O(n)
# Space Complexity :- O(1)



def majorityelement2(nums):
    n=len(nums)
    result=[]

    element1=0
    element2=0
    count1=0
    count2=0
    element1count=0
    element2count=0

    for i in range (n):

        if count1==0 and nums[i]!=element2:
            element1=nums[i]
            count1=1
        elif count2==0 and nums[i]!=element1:
            element2=nums[i]
            count2=1
        elif element1==nums[i]:
            count1+=1
        elif element2==nums[i]:
            count2+=1
        else:
            count1-=1
            count2-=1
    for i in range (n):
        if nums[i]==element1:
            element1count+=1
        elif nums[i]==element2:
            element2count+=1
    if element1count>n//3:
        result.append(element1)
    if element2count>n//3:
        result.append(element2)
    return result


print(majorityelement2([1, 2, 1, 3,1,2]))