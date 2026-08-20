def mergetwosortedarrayswithoutusingextraspace(nums1,nums2):
    m=len(nums1)
    n=len(nums2)

    i=m-1
    j=0

    while i>=0 and j<n:
        if nums1[i]>nums2[j]:
            nums1[i],nums2[j]=nums2[j],nums1[i]
            i-=1
            j+=1
        else:
            break
    nums1.sort()
    nums2.sort()

    return nums1,nums2

print(mergetwosortedarrayswithoutusingextraspace([-5,-2,4,5],[-3,1,8]))