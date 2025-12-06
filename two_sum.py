def two_sum_sorted(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        if arr[low] + arr[high] == target:
            return low + 1 , high + 1
        
        elif arr[low] + arr[high] > target:
            high -= 1
        else:
            low += 1
    
    return -1

print(two_sum_sorted( [1,2,3,4,4,9,56,90], target = 8))