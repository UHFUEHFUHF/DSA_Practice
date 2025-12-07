def first_unique(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for key , value in  freq.items():
        if value == 1:
            return key
print(first_unique([4,5,1,2,1,2,5]))