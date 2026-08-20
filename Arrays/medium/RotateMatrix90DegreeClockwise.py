# Brute Force Approach :-
# Time Complexity :- O(n^2)
# Space Complexity :- O(n^2)


# def rotatematrix90degreeclockwise(matrix):
#     n=len(matrix)

#     result=[[0]*n for _ in range (n)]

#     for i in range (n):
#         for j in range (n):
#             result[j][n-1-i]=matrix[i][j]

#     return result



# Optimal Approach :-
# Time Complexity :- O(n^2)
# Space Complexity :- O(1)


def rotatematrix90degreeclockwise(matrix):
    n=len(matrix)

    for i in range (n):
        for j in range (i+1,n):
            matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
    for i in range (n):
        left=0
        right=n-1

        while left<right:
            matrix[i][left],matrix[i][right]=matrix[i][right],matrix[i][left]
            left+=1
            right-=1
    return matrix

print( rotatematrix90degreeclockwise([[0, 1, 1, 2], 
                                      [2, 0, 3, 1], 
                                      [4, 5, 0, 5], 
                                      [5, 6, 7, 0]]))