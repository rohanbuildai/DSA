def countsubarraywith_XOR_K(nums,k):
    n=len(nums)
    XOR=0
    hashmap={0:1}
    count=0

    for i in range (n):
        XOR^=nums[i]
        x=XOR^k

        if x in hashmap:
            count+=hashmap[x]
        if XOR in hashmap:
            hashmap[XOR]+=1
        else:
            hashmap[XOR]=1
    return count

print(countsubarraywith_XOR_K( [4, 2, 2, 6, 4],6))