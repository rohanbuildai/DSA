def n_meetings_in_one_room(start,end) :
    n = len(start)
    previous = -1
    i = 0
    j = 0
    count = 0

    meetings = sorted(zip(start, end), key=lambda x: x[1])
    start = [x[0] for x in meetings]
    end = [x[1] for x in meetings]

    while i < n:
        if start[i] <= previous:
            i += 1
            j += 1
        elif start[i] > previous:
            count += 1
            previous = end[j]
            i += 1
            j += 1

    return count

print(n_meetings_in_one_room( [10, 12, 20],[20, 25, 30]))