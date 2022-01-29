
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        if nums[lo] == target:
            return lo
        elif nums[hi] == target:
            return hi
        # mid = lo
        
        while(lo < hi-1):
            mid = int((lo + hi) / 2)
            if target > nums[mid]:
                lo = mid
            elif target < nums[mid]:
                hi = mid
            else:
                return mid
        
        return -1 
            
        


def main():
    # test_input = [-1,0,3,5,7,12, 16]
    test_input = [-1,0]
    target = 1
    bs = Solution()
    print(bs.search(test_input, target))
    
    
                 
if __name__ == "__main__":
    main()