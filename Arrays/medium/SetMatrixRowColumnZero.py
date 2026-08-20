# Brute Force :-
# Time Complexity - O(n^3)

# def setmatrixrowclomnzero(matrix):
#     m=len(matrix)
#     n=len(matrix[0])


#     for i in range (m):
#         for j in range(n):
#             if matrix[i][j]==0:
#                 for k in range (m):
#                     if matrix[k][j]!=0:
#                         matrix[k][j]=-1
#                 for l in range (n):
#                     if matrix[i][l]!=0:
#                         matrix[i][l]=-1
#     for x in range (m):
#         for y in range (n):
#             if matrix[x][y]==-1:
#                 matrix[x][y]=0
#     return matrix






# Better :-
# Time Complexity :- O(2mn)
# Space Complexity :- O(m+n)

# def setmatrixrowclomnzero(matrix):
#     m=len(matrix)
#     n=len(matrix[0])

#     row=[0]*m
#     column=[0]*n

#     for i in range (m):
#         for j in range (n):
#             if matrix[i][j]==0:
#                 row[i]=1
#                 column[j]=1
#     for k in range (m):
#         for l in range (n):
#             if row[k]==1 or column[l]==1:
#                 matrix[k][l]=0
#     return matrix




# Optimal :-
# Time Complexity :- O(MxN)
# Space Complexity :- O(1)

def setmatrixrowclomnzero(matrix):
    m=len(matrix)
    n=len(matrix[0])

    col_0=1

    for i in range (m):
        for j in range (n):
            if matrix[i][j]==0:
                matrix[i][0]=0
                if j!=0:
                    matrix[0][j]=0
                else:
                    col_0=0
    for i in range (1,m):
        for j in range (1,n):
            if matrix[i][j]!=0:
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
    if matrix[0][0]==0:
        for j in range (n):
            matrix[0][j]=0
    if col_0==0:
        for i in range (m):
            matrix[i][0]=0
    return matrix




print(setmatrixrowclomnzero([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))