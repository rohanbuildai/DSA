# Optimal Approach :-
# Time Complexity :- O(n)
# Space Complexity :- O(1)
def rightrotatearraybyone(nums,k):
    
    n=len(nums)
    k%=n

    i=0
    j=n-1

    m=0
    p=k-1

    x=k
    y=n-1

    while i<j:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
    while m<p:
        nums[m],nums[p]=nums[p],nums[m]
        m+=1
        p-=1
    while x<y:
        nums[x],nums[y]=nums[y],nums[x]
        x+=1
        y-=1
    return nums






print(rightrotatearraybyone([1,2,3,4,5,6,7],3))