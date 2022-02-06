# 557. Reverse Words in a String III

class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        result =  ""
        for y in x:
            result = result + y[::-1] + " "
            
            
        return result[:-1]