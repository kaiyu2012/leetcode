# 283. Move Zeroes

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x=0
        for i in range(len(nums)):
            if nums[i]:
                nums[x] = nums[i]
                x += 1
        nums[x:] = [0] * (len(nums) - x)