def isAnagram(s, t):
    freqs = {}
    freqt = {}
    for i in s:
        if i in freqs:
            freqs[i] += 1
        else:
            freqs[i] = 1
        
    for j in t:
        if j in freqt:
            freqt[j] += 1
        else:
            freqt[j] = 1
    
    if freqt == freqs:
        return True
    else:
        return False
    
    
    

print(isAnagram(s = "rat", t = "car"))