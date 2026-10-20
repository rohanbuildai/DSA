def fractional_knapsack(val,wt,capacity) :
    items = []

    n = len(val)

    for i in range (n) :
        ratio = val[i] / wt[i]
        items.append((ratio,val[i],wt[i]))
    items.sort(reverse=True)

    remaining = capacity
    ans = 0

    for ratio,value,weight in items :
        if remaining == 0 :
            break
        elif weight <= remaining :
            ans += value
            remaining -= weight
        else :
            ans += ratio * remaining
            remaining = 0
    return ans

print(fractional_knapsack([60,100,120],[10,20,30],50))