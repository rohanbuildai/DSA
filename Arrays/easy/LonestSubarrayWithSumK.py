def longestsubarraywithsumk(arr,k):
    n=len(arr)
    current_sum=0
    length=0
    i=0
    j=0

    while (j<n):
        current_sum+=arr[j]

        while current_sum>k:
            current_sum-=arr[i]
            i+=1
        if current_sum==k:
            length=max(length,j-i+1)
        j+=1
    return length


print(longestsubarraywithsumk([1,2,1,2,1],3))