def insert_interval(intervals,new_interval) :
    n = len(intervals)
    ans = []
    first_overlapping_element = new_interval[0]
    last_overlapping_element = new_interval[1]

    for i , j in intervals :
        if ( i <= new_interval[1] and j >= new_interval[0] ) :
            first_overlapping_element = min(first_overlapping_element,i)
            last_overlapping_element = max(last_overlapping_element,j)
        else :
            ans.append([i,j])

    merged = [first_overlapping_element,last_overlapping_element]

    for k in range (len(ans)) :
        if ans[k][0] > merged[0] :
            ans.insert(k,merged)
            break
    else :
        ans.append(merged)

    return ans

print( insert_interval( [[6, 8], [10, 12]] , [1,4] ) )