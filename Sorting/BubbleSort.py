# def Bubble_Sort(Arr):
#     n=len(Arr)

#     for i in range (0,n-1):
#         for j in range(i+1,n):
#             if Arr[j]<Arr[i]:
#                 Arr[i],Arr[j]=Arr[j],Arr[i]
#     return Arr


# print(Bubble_Sort([1,6,2,9,3,5,9,6,5]))



def bubblesort(arr, i=0,j=1):
    n=len(arr)

    if arr[j]<arr[i]:
        bubblesort(arr,i)

    