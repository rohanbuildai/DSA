def countinversions(nums):
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
        temp=[]
        left=low
        right=mid+1

        while left<=mid and right<=high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                count+=(mid-left)+1
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

print(countinversions([5,3,2,4,1]))