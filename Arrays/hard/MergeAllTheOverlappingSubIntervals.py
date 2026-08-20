# Optimal Solution :-
# TIme Complexity :- O(n log n)
# Space Complexity :- O(1)
def mergealltheoverlappingsubintervals(intervals):
    m=len(intervals)
    intervals.sort( )

    ans=[]

    current_interval=[intervals[0][0],intervals[0][1]]

    for i in range (1,m):
        if intervals[i][0] <= current_interval[1]:
            current_interval[1]=max(current_interval[1],intervals[i][1])
        else:
            ans.append(current_interval)
            current_interval=[intervals[i][0],intervals[i][1]]
    ans.append(current_interval)
    return ans
print(mergealltheoverlappingsubintervals( [[1,5],[3,6],[8,10],[15,18]]))