def merge_sorted_lists(arr1, arr2):
    new_sorted = []
    i, j = 0, 0
    
   
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_sorted.append(arr1[i])
            i += 1
        else:
            new_sorted.append(arr2[j])
            j += 1
    
    
    while i < len(arr1):
        new_sorted.append(arr1[i])
        i += 1
    
   
    while j < len(arr2):
        new_sorted.append(arr2[j])
        j += 1
    
    return new_sorted

print(merge_sorted_lists(arr1=[1, 3, 5], arr2=[2, 4, 6])) 