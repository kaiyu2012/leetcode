
from typing import List

def is_bad_version(version):
    if version >= 1:
        return True
    else:
        return False

class Solution:
    def first_bad_version(self, n: int) -> int:
        lo, hi = 1, n
        while(lo < hi-1):
            mid = (lo+hi) >> 1
            if(is_bad_version(mid)):
                hi = mid
            else:
                lo = mid
        
        if is_bad_version(lo):
            return lo
        return hi
            
        


def main():
    fb = Solution()
    print(fb.first_bad_version(1))
    
    
                 
if __name__ == "__main__":
    main()