def Selection_Sort(arr):
    n=len(arr)

    for i in range (0,n-1):
        min=i

        for j in range (i,n):
            if arr[j]<arr[min]:
               min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr

print(Selection_Sort([23,40,10,45,3,2,1]))
