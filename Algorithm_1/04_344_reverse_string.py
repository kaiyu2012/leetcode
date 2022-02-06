# 344. Reverse String

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        x, y = 0, len(s)-1
        while(x<y):
            t = s[x]
            s[x] = s[y]
            s[y] = t
            x += 1
            y -= 1