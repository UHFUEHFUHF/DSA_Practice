def Deletion(arr , k):
    n = len(arr) - 1
    for i in range(k , n):
       arr[i] = arr[i + 1]
    
    arr.pop()  
    return arr

print(Deletion([1,23,45,290,67,89,57,45], 4))