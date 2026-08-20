def countsubarrayswithgivenSum(arr,k):
    n=len(arr)
    sum=0
    hashmap={0:1}
    count=0

    for i in range (n):
        sum += arr[i]
        more = sum-k

        if more in hashmap:
            count+=hashmap[more]
        if sum in hashmap:
            hashmap[sum]+=1
        else:
            hashmap[sum]=1
    return count

print(countsubarrayswithgivenSum([1,1,1],2))