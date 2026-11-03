# def fruits_into_baskets(fruits) :
#     n = len(fruits)

#     max_length = 0

#     for i in range (n) :
#         frequency = set()
#         for j in range (i,n) :
#             frequency.add(fruits[j])

#             if len(frequency) <= 2 :
#                 max_length = max(max_length,j-i+1)
#             else :
#                 break
#     return max_length

# print(fruits_into_baskets([1,2,3,2,2]))

def fruits_into_baskets(fruits) :
    n = len(fruits)

    hash_array = {}
    max_length = 0
    start = 0
    end = 0

    while end < n :
        if fruits[end] in hash_array :
            hash_array[fruits[end]] += 1
        else :
            hash_array[fruits[end]] = 1

        if len(hash_array) > 2 :
            while len(hash_array) > 2 :
                hash_array[fruits[start]] -= 1
                if hash_array[fruits[start]] == 0 :
                    hash_array.pop(fruits[start])
                start += 1
        if len(hash_array) <= 2 :
            max_length = max(max_length,end-start+1)
        end += 1
    return max_length


print(fruits_into_baskets([1,2,3,2,2]))