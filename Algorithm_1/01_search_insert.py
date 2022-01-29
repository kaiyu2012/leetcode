
from typing import List

class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        if target > nums[hi]: return hi + 1
        elif target <= nums[lo]: return lo
        while(lo < hi-1):
            mid = (lo+hi) >> 1
            if(nums[mid] < target):
                lo = mid
            else:
                hi = mid
        
  
        return hi
            
        


def main():
    nums = [1,3,5,6]
    target = 1
    si = Solution()
    print(si.search_insert(nums, target))
    
    
                 
if __name__ == "__main__":
    main()