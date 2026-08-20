def removeduplicatesfromthesortedarray(arr):
    n=len(arr)
    unique=arr[0]
    uniquecounter=1

    for i in range (1,n):
        if arr[i]!=unique:
            unique=arr[i]
            arr[uniquecounter]=arr[i]
            uniquecounter+=1
    return uniquecounter,arr

print(removeduplicatesfromthesortedarray([1,1,2]))