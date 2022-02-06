# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = 0
        pos = 0
        test = {}
        for i in range(0, len(s)):
            # print(test)
            x = s[i]
            if x in test:
                test[x] += 1               
            else:
                test[x] = 1            
            if len(test) > w:
                w += 1
            else:
                test[s[pos]] -= 1
                if test[s[pos]] == 0:
                    del test[s[pos]]
                pos += 1
                
        # print(w)
        
        return w