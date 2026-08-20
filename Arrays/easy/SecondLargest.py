def secondLargestElement(nums):
        largest=nums[0]
        secondlargest=-1

        for i in range (1,len(nums)):
            if nums[i]>largest:
                secondlargest=largest
                largest=nums[i]
            elif nums[i]!=largest and nums[i]>secondlargest:
                 secondlargest=nums[i]

        return secondlargest        

print(secondLargestElement([8,8,7,6,5]))   