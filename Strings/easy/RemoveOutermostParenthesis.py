def removeoutermostparenthesis(s):
    n=len(s)

    balance = 0
    ans = ""

    for char in s:
        if char == ")" :
            balance -= 1
        if balance != 0:
            ans += char
        if char == "(" :
            balance += 1
    return ans

print(removeoutermostparenthesis("((()))"))