def containsDuplicate(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for  i in freq.values():
        if i >= 2:
            return True
            
    return False
    
    

print(containsDuplicate( [1,2,3,1]))