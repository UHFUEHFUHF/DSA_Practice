def twoSum(nums, target):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for key in freq:
        comp = target - key
        if comp in freq:
            return comp

print(twoSum([2,7,11,15], target = 9))
    