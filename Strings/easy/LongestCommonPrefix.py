def longestcommonprefix(strs):
    n=len(strs)
    m=len(strs[0])
    ans = ""

    current_char = strs[0][0]

    for i in range (m):
        count=1
        for j in range (n):
            if current_char == strs[j][i]:
                count+=1

        if count == n:
            ans+=current_char
            current_char = strs[j][i]

print(longestcommonprefix( ["flowers" , "flow" , "fly", "flight" ]))