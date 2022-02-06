
# 567. Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        
        if l1 > l2:
            return False
        
        d1 = {}
        d2 = {}
        
        for i in range(0, l1):
            x = s1[i]
            if x in d1:
                d1[x] += 1
            else:
                d1[x] = 1
            
            y = s2[i]
            if y in d2:
                d2[y] += 1
            else:
                d2[y] = 1
                
        if d2 == d1:
            return True
        
        j = 0
        
        for i in range(l1, len(s2)):
        
            d2[s2[j]] -= 1
            if d2[s2[j]] == 0:
                del d2[s2[j]]
            if s2[i] in d2:
                d2[s2[i]] += 1
            else:
                d2[s2[i]] = 1
                
            if d2 == d1:
                return True
                      
            j += 1
            
           
            
        return False
            
            
            
        