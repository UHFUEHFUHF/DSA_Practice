def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] , nums[j] = nums[j] , nums[i]
            i += 1
        
        
    return nums[:i]

print(removeElement([1 , 2 , 2 , 3] , 3) )