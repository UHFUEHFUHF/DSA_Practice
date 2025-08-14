def Insert(arr , k , element):
    arr.append(None)
    n = len(arr) - 2
    i = n
    while i >= k:
        arr[i + 1] = arr[i]
        i -= 1
    arr[k] = element
    return arr

print(Insert([10,20,30,40] , 2 , 99))