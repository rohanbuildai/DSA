def max_consecutive_ones_three(nums, k):
    n = len(nums)

    start = 0
    zero_count = 0
    final_count = 0

    for end in range(n):

        if nums[end] == 0:
            zero_count += 1

        if zero_count > k:

            if nums[start] == 0:
                zero_count -= 1

            start += 1

        final_count = max(final_count, end - start + 1)

    return final_count


print(max_consecutive_ones_three(
    [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3
))