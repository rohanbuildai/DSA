def painterspartition(A,B,C):
    n=len(C)

    low=max(C)
    high=sum(C)
    ans=0

    if A > n:
        return max(C)

    while (low<=high):
        mid=(low+high)//2

        if countSubarrays(C,mid) <= A:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return (ans * B) % 10000003 
def countSubarrays(C,count):
    n=len(C)
    subarray=1
    currentSum=0

    for i in range (n):

        if currentSum + C[i] <= count:
            currentSum+=C[i]
        else:
            subarray+=1
            currentSum=C[i]
    return subarray

print(painterspartition(10,1,[1, 8, 11, 3]))