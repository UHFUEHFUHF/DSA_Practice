def Deletion(arr , k ):
    n = len(arr) - 1 ## 7 - 1 = 6
    i = k
    while(i < n):
        arr[i] = arr[i + 1]
        i += 1
    
    print(arr)
    
Deletion([2,3,544,3,2,245,45] , 2)