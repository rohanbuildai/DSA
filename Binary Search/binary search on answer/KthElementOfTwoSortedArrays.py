def kthelementoftwosortedarrays(nums1,nums2,k) :

    if len(nums1) > len(nums2):
        nums1,nums2=nums2,nums1

    n1=len(nums1)
    n2=len(nums2)

    low=max(k-n2,0)
    high=min(k,n1)

    left_side_should_contribute = k

    while (low<=high):
        cut1=(low+high) // 2
        cut2=left_side_should_contribute - cut1
        l1=float("-inf") if cut1==0 else nums1[cut1 - 1]
        r1=float("inf") if cut1==n1 else nums1[cut1]
        l2=float("-inf") if cut2==0 else nums2[cut2 - 1]
        r2=float("inf") if cut2==n2 else nums2[cut2]

        if l1<=r2 and l2<=r1:
                return max(l1,l2)
        elif l1>r2:
            high = cut1 - 1
        else:
            low=cut1+1

print(kthelementoftwosortedarrays([2, 3, 6, 7, 9],[1, 4, 8, 10,11],5))