import math

def shortest_job_first(bt) :
    bt.sort()
    n = len(bt)

    time = 0
    prev_burst = 0
    ans = 0

    for i in range (n) :
        time = prev_burst + time
        prev_burst = bt[i]
        ans = ans + time
    
    return math.floor(ans/n)

print(shortest_job_first([1,2,3,4]))  # 1,2,3,4,7