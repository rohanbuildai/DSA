def unionoftwoarrays(nums1,nums2):
    result=[]
    n1=len(nums1)
    n2=len(nums2)

    i=0
    j=0

    while (i<n1 and j<n2):
        if nums1[i]<nums2[j]:
            result.append(nums1[i])
            i+=1
        elif nums1[i]>nums2[j]:
            result.append(nums2[j])
            j+=1
        else:
            result.append(nums1[i])
            j+=1
            i+=1
    while i<n1:
        result.append(nums1[i])
        i+=1
    while j<n2:
        result.append(nums2[j])
        j+=1

    return result

print(unionoftwoarrays([1,2,3,4,5],[1,2,7]))