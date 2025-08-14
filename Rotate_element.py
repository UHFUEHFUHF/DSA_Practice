def Rotate(arr):
    n = len(arr) - 1
    first = arr[0]
    i = 0 
    while i < n:
        arr[i] = arr[i + 1]
        i += 1
    
    arr[n] = first
    return arr

print(Rotate([1, 2, 3, 4, 5]))
    