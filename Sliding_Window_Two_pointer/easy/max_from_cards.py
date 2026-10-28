def max_from_cards(cardScore,k) :
    n = len(cardScore)
    sum_of_array = sum(cardScore)

    if n == k :
        return sum_of_array

    window = n-k
    current_window_sum = sum(cardScore[:window])
    maximum_sum = sum_of_array - current_window_sum

    for i in range (1,k+1) :
        current_window_sum -= cardScore[i-1]
        current_window_sum += cardScore[i + (window-1)]
        maximum_sum = max(maximum_sum,sum_of_array-current_window_sum)

    return maximum_sum

print(max_from_cards([1, 2, 3, 4, 5, 6, 1], 3))