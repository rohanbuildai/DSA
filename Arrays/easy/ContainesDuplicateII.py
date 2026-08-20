def containesduplicateII(arr,k):
    n=len(arr)
    hashmap={}

    for i in range (n):
        if arr[i] not in hashmap:
            hashmap[arr[i]]=i
        elif arr[i] in hashmap:
            if abs(hashmap[arr[i]]-i)<=k:
                return True
            else:
                hashmap[arr[i]]=i
    return False

print(containesduplicateII([1,2,3,1,2,3],2))