# Brite Force :-
# Space :- O(1)
# Time :- O(n^2)


# def findtherepeatingandmissingnummber(nums):
#     n=len(nums)
#     missing=-1
#     repeating=-1

#     for i in range (1,n+1):
#         count=0
#         for j in range (n):
#             if nums[j]==i:
#                 count+=1
#         if count==2:
#             repeating=i
#         elif count==0:
#             missing=i
#     return repeating,missing
    

# print(findtherepeatingandmissingnummber( [1, 2, 3, 6, 7, 5, 7]))



# Optimal Approach :-
# Time :- O(n)
# Space :- O(1)




# def findtherepeatingandmissingnummber(nums):
#     n=len(nums)
#     S1=0
#     Sn1=(n*(n+1)) // 2
#     S2=0
#     Sn2=(n*(n+1)*(2*n+1)) // 6

#     for i in range (n):
#         S1+=nums[i]
#         S2+=nums[i]*nums[i]


#     val1=Sn1-S1  # x-y
#     val2=Sn2-S2
#     val2=val2//val1

#     x=(val1+val2) //2
#     y=x-val1

#     return x,y



# print(findtherepeatingandmissingnummber( [1, 2, 3, 6, 7, 5, 7]))













def findthemissingandrepeatingnumber(nums):
    n=len(nums)

    i=0
    missing_number = 0
    repeating_number = 0

    while (i<n) :
        while nums[i] <= n and nums[i] != nums[nums[i]-1] :
            correct = nums[i]-1
            nums[i],nums[correct] = nums[correct] , nums[i]
        i+=1

    for i in range (n):
        if nums[i] != i+1 :
            return i+1 , nums[i]
print(findthemissingandrepeatingnumber( [3, 5, 4, 1, 1]))