# 1 :- given row and column print the element at that place , R=5 C=3

# def pascalstriangle1(r,c):

#     ans=1

#     for i in range (1,c):
#         ans=ans*(r-i)
#         ans=ans//(i)
#     return ans
# R=5
# C=3
# print(pascalstriangle1(R-1,C-1))

# 2 :- print any nth row of pascals triangle

def pascalstriangle2(n):
    ans=1
    result=[]
    result.append(ans)
    for i in range (1,n+1):
        ans=ans*((n+1)-i)
        ans=ans//i
        result.append(ans)
    return result
print(pascalstriangle2(3))

# 3 :- print whole pascals triangle for given n

# def pascalstriangle3(n):
#     result=[]

#     for i in range (1,n+1):
#         result.append(pascalstriangle2(i))
#     return result
# print(pascalstriangle3(5))