def Bubble_Sort(arr):
    l = len(arr)
    for i in range(l):
        swapped = False
        for j in range(0 , l-i-1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j+1] = arr[j + 1] , arr[j]
                swapped = True
        if not swapped:
            break
    return arr
    

print(Bubble_Sort([5,8,2,4,9,1,4,2]))
    