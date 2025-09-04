def good_letters(s):
    from collections import defaultdict
    
    counts = defaultdict(int)  
    
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        if j - i >= 2:
            counts[s[i]] += 1
        i = j
    
    result = sorted([ch for ch, cnt in counts.items() if cnt == 1])
    return "".join(result)



print(good_letters("bbbccbbbaa"))  
print(good_letters("xyzxyz"))      
print(good_letters("aabb"))        
print(good_letters("aabbaabb"))  