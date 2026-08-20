def findnthrootofanumber(N,M):
    low=1
    high=M

    while (low<=high):
        mid=(low+high)//2

        if mid**N==M:
            return mid
        elif mid**N<M:
            low=mid+1
        else:
            high=mid-1
    return -1


print(findnthrootofanumber(2,64))