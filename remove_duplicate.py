def remove_duplicates(nums):
    i = 0
    new = []
    for j in range(0 , len(nums) , 1):
        if nums[i] == nums[j]:
            if nums[j] not in new:
                new.append(nums[j])
            i += 1
    
    return new

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
        
            