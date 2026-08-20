# number hashing:-

# n=int(input("enter the number of elements"))
# arr=[]
# for _ in range (n):
#     arr.append(int(input("enter elements")))

# hash_array=[0]*13

# for num in arr:
#     hash_array[num]+=1

# q=int(input("enter the number of queries"))

# while(q>0):
#     number=int(input("enter quieries"))

#     print(f"number of times {number} appeared : {hash_array[number]}")
#     q-=1

# character hashing:-

# String=input("enter a string")
# Hash_map=[0]*26

# for s in String:
#     Hash_map[ord(s)-ord('a')]+=1
# q=int(input("number of queries"))

# while(q>0):
#     character=input("enter a query")
#     print(f"number of times {character} appeared {Hash_map[ord(character)-ord('a')]}")
#     q-=1











# n=int(input("entter the number of elements "))
# arr=[]
# for _ in range (n):
#     arr.append(int(input("enter elements")))
# hash_table=[0]*13
# for num in arr:
#     hash_table[num]+=1
# q=int(input("enter the no of queries"))

# while (q>0):
#     number=int(input("enter queries"))
#     print(f"number of times {number} appears is {hash_table[number]}")
#     q-=1



def countFrequencies(nums):
        result=[]
        hash_table=[0]*13
        for num in nums:
            hash_table[num]+=1
        for i in range(len(hash_table)):
            if hash_table[i] > 0:
              result.append([i, hash_table[i]])
        return result


print(countFrequencies([1,2,2,1,3]))