def is_sorted(arr):
    first = arr[0]
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
        
    return True

print(is_sorted([1, 3, 2, 4]))