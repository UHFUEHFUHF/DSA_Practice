def first_occurrence(arr, target):
    answer = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            answer = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return answer        




def last_occurrence(arr, target):
    answer = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            answer = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return answer            
            


# Example usage:
arr = [2, 4, 4, 4, 8, 10]
target = 4
print("First Occurrence:", first_occurrence(arr, target))  # Expect 1
print("Last Occurrence:", last_occurrence(arr, target))    # Expect 3
