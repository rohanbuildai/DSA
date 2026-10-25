def minimum_number_of_platforms_required_for_railway(arrival,departure) :
    arrival.sort()
    departure.sort()
    n = len(arrival)
    i = 1
    j = 0

    platform = 1
    max_platform = 1

    while i < n and j < n :
        if arrival[i] <= departure[j] :
            platform += 1
            max_platform = max(platform,max_platform)
            i += 1
        else :
            platform -= 1
            j += 1
    return max_platform

            

print(minimum_number_of_platforms_required_for_railway([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000]))