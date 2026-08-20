# def Insertion_Sort(Arr):
#     n=len(Arr)

#     for i in range (1,n):
#         key=Arr[i]

#         j=i-1

#         while (j>=0 and key<Arr[j]):
#             Arr[j+1]=Arr[j]
#             j-=1
#         Arr[j+1]=key




#     return Arr

# print(Insertion_Sort([2,6,3,56,4,76,8,9,67,4,3,56]))    














# def Insertionsort(Arr):
#     n=len(Arr)

#     for i in range (1,n):
#         j=i-1
#         key=Arr[i]

#         while (j>=0 and key<=Arr[j]):
#             Arr[j]=Arr[j+1]
#             j-=1

#         Arr[j+1]=key
#     return Arr
# print(Insertionsort([2,5,6,4,3,5,7,7,5,4,4,8]))


def inertionsort(arr):
    n=len(arr)

    for i in range (1,n):
        key=arr[i]
        j=i-1

        while ( j>=0 and key<=arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
        
print(inertionsort([1,4,3,6,8,3,4,5,6]))