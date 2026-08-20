def kidswiththegreatestnumberofcandies(candies,extraCandies):
    n=len(candies)
    Maximum=max(candies)

    for i in range (n):
        Sum=candies[i]+extraCandies
        if Sum>=Maximum:
            candies[i]=True
        else:
            candies[i]=False
    return candies


print(kidswiththegreatestnumberofcandies([4,2,1,1,2],1))