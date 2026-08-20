def arrangeelementbysign(arr):
    n=len(arr)
    pos=0
    neg=1

    ans=[0]*n

    for x in arr:
        if x >0:
            ans[pos]=x
            pos+=2
        else:
            ans[neg]=x
            neg+=2
    return ans

    



print(arrangeelementbysign([-1,-2,1,2]))