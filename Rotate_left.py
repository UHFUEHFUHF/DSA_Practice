def Rotate(arr):
    n = len(arr) - 1
    last = arr[n]
    i = n
    while i > 0:
        arr[i] = arr[i - 1]
        i -= 1
    
    arr[0] = last
    return arr

print(Rotate([1, 2, 3, 4, 5]))
    