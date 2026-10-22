def non_overlapping_intervals(intervals) :
    intervals.sort(key=lambda x: x[1])
    previous = intervals[0][1]
    count = 0

    for i , j in intervals[1:] :
        if i < previous :
            count += 1
        else :
            previous = j
    return count

print(non_overlapping_intervals( [ [1, 3] , [1, 4] , [3, 5] , [3, 4] , [4, 5] ]))