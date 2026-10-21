def job_sequencing(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: x[2], reverse=True)
    slot = [-1] * n
    count_profit = 0
    count = 0

    for id,deadline,profit in jobs :
        deadline = min(deadline,n)
        if slot[deadline-1] == -1 :
            slot[deadline-1] = id
            count_profit += profit
            count += 1
        else :
            for i in range (deadline-1,-1,-1) :
                if slot[i] == -1 :
                    slot[i] = id 
                    count_profit += profit
                    count += 1
                    break
    return (count,count_profit)

print(job_sequencing([
    [1, 1, 50],
    [2, 2, 20],
    [3, 3, 30],
    [4, 4, 10]
]))