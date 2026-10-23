def merge_intervals(intervals) :
    intervals.sort()
    n = len(intervals)
    start_1 = intervals[0][0]
    end_1 = intervals[0][1]
    ans = []

    for start_2 , end_2 in intervals[1:] :
        if start_2 <= end_1 :
            start_1 = min(start_1,start_2)
            end_1 = max(end_1,end_2)
        else :
            ans.append([start_1,end_1])
            start_1 = start_2
            end_1 = end_2
    ans.append([start_1,end_1])

    return ans

print(merge_intervals( [[1,3],[2,6],[8,10],[15,18]]))