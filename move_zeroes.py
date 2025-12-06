def move_zeroes(arr):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        
        if arr[low] == 0:
            arr[low] , arr[high] = arr[high] , arr[low]
            high -= 1
        else:
            low += 1
    
    return arr

print(move_zeroes([0, 1, 0, 3, 12]))