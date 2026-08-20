# def partition(arr,low,high):
#     pivot=arr[low]

#     i=low
#     j=high

#     while i<j:
#         while i<=high and arr[i]<=pivot:
#             i+=1
#         while arr[j]>pivot:
#             j-=1
#         if i<j:
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[low],arr[j]=arr[j],arr[low]
#     return j

# def quicksort(arr,low,high):
    
#     if low<=high:
#         p=partition(arr,low,high)

#         quicksort(arr,low,p-1)
#         quicksort(arr,p+1,high)

#     return arr

# arr=[4,6,2,5,7,9,1,3]
# print(quicksort(arr,0,len(arr)-1))




def partition(arr,low,high):

    pivot=arr[low]

    i=low
    j=high

    while i<j:
        while (i<=high and arr[i]<=pivot):
            i+=1
        while (arr[j]>pivot):
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quicksort(arr,low,high):

    if low<=high:

        p=partition(arr,low,high)

        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)

    return arr


arr=[3,6,4,23,56,56,745,67,567,56]
print(quicksort(arr,0,len(arr)-1))