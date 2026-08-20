def largestoddnumberinastring(s):

    n=len(s)
    ans=""

    element1=0
    element2=0

    for i in range (n):
        if int(s[i]) !=0 :
            element1=i
            break
    for i in range (n-1,-1,-1):
        if int(s[i]) %2 !=0:
            element2=i
            break

    if element1 == -1 or element2 == -1 or element1 > element2:
        return ""

    return s[element1:element2 + 1]

    


print(largestoddnumberinastring("0032579"))