def lemonade_change(bills) :
    n = len(bills) 

    dollar_5 = 0
    dollar_10 = 0

    for i in range (n) :
        if bills[i] == 5 :
            dollar_5 += 1
        elif bills[i] == 10 :
            if dollar_5 == 0 :
                return False
            dollar_5 -= 1
            dollar_10 += 1
        else :
            if dollar_10 > 0 and dollar_5 > 0:
                dollar_10 -= 1
                dollar_5 -= 1
            elif dollar_5 >= 3:
                dollar_5 -= 3
            else:
                return False

    return True

print(lemonade_change([5, 5, 10, 5, 20, 5, 10, 20]))