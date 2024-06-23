def findTheDifference(s, t):
    count_s = {}
    count_t = {}
    
    for char in s:
        if char in count_s:
            count_s[char] += 1
        else:
            count_s[char] = 1
    
    for char in t:
        if char in count_t:
            count_t[char] += 1
        else:
            count_t[char] = 1
    
    for char in count_t:
        if char not in count_s or count_t[char] > count_s[char]:
            return char
    
    return None

s = "abcd"
t = "abcde"
print(findTheDifference(s, t)) 
