import string

def isPalindrome(s):
    cleaned_text = ""
    for i in s.lower():
        if i not in string.punctuation and i not in " ":
            cleaned_text += i
    
    l, j = 0, len(cleaned_text) - 1
    
    while l < j:
        if cleaned_text[l] != cleaned_text[j]:
            return False
        l += 1
        j -= 1
    
    return True

print(isPalindrome(s = "race a car"))  
print(isPalindrome(s = "A man, a plan, a canal: Panama"))  