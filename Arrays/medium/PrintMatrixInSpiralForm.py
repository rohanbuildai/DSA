# Time Complexity :- O(mxn)

def printmatrixinspiralform(matrix):
    m=len(matrix)
    n=len(matrix[0])
    result=[]

    top=0
    left=0
    right=n
    bottom=m

    while top<bottom and left<right:

        for i in range (left,right):
           result.append(matrix[top][i])
        top+=1
        for i in range (top,bottom):
            result.append(matrix[i][right-1])
        right-=1
        if top<bottom:
            for i in range (right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            bottom-=1
        if left<right:
            for i in range (bottom-1,top-1,-1):
                result.append(matrix[i][left])
            left+=1
    return result
print(printmatrixinspiralform( [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]))