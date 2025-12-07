def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1 , len(nums)):
            if nums[i] + nums[j] == target:
                return i , j
    
    return -1

print(twoSum([2,4,5,9,3,5] , 10))