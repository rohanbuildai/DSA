def leadersinanarray(arr):
    n=len(arr)
    result=[]
    result.append(arr[n-1])

    current_highest=arr[n-1]

    j=n-1

    while j>0:
            if arr[j-1]>current_highest:
                result.append(arr[j-1])
                current_highest=arr[j-1]
                j-=1
            else:
                j-=1
    result.reverse()
    return result

print(leadersinanarray([10, 9, 8, 11]))