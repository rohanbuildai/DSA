# def reverseeverywordinastring(s):
#     n=len(s)

#     words=s.split()

#     words.reverse()

#     ans = " ".join(words)

#     return ans

# print(reverseeverywordinastring("welcome to the jungle"))


nums=[3,7]   # 2,3,4,5
nums.sort()
n=len(nums)

print (((nums[n-1])-1) *(( nums[n-2])-1))
