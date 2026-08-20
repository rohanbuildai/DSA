def countreversepairs(nums):
    n=len(nums)
    count=0

    def mergesort(nums,low,high):

        if low>=high:
            return
        
        mid=(high+low)//2

        mergesort(nums,low,mid)
        mergesort(nums,mid+1,high)
        merge(nums,low,mid,high)

    def merge(nums,low,mid,high):
        nonlocal count
        i=low
        j=mid+1
        temp=[]
        left=low
        right=mid+1

        while i<=mid:
            while j<=high and nums[i] > 2*nums[j]:
                j+=1
            count+=j-(mid+1)
            i+=1

        while left<=mid and right<=high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=high:
            temp.append(nums[right])
            right+=1
        for i in range (len(temp)):
            nums[low+i]=temp[i]

    mergesort(nums,0,n-1)
    return count

print(countreversepairs([6,4,1,2,7]))