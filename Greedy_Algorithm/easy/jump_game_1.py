def jump_game_1(nums) :
    n = len(nums)
    max_reach = 0

    for i in range (n-1) :
        if i > max_reach :
            return False
        current_reach = i + nums[i]
        max_reach = max(max_reach,current_reach)

    return max_reach , max_reach >= n-1

print(jump_game_1([3,0,8,2,0,0,1]))