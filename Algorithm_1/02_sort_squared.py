from typing import List

class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        sq0 = []
        sq1 = []
        for x in nums:
            if (x<0):
                sq0.insert(0, x*x)
            else: 
                sq1.append(x*x)
        ssq = []
        x, y = 0, 0
        lx, ly = len(sq0), len(sq1)
        for _ in range(len(nums)):
            if x < lx and y < ly:
                if sq0[x] > sq1[y]:
                    ssq.append(sq1[y])
                    y += 1
                else:
                    ssq.append(sq0[x])
                    x += 1
            elif x >= lx and y < ly:
                ssq += sq1[y:]
                break
            elif x < lx and y >= ly:
                ssq += sq0[x:]
                break
            
        return ssq
                
 
class Solution_second:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        ssq = []
        x, y = 0, 0
        for i in range(0, len(nums)):
            sq = nums[i] * nums[i]
            if (nums[i]<0):
                print(f'{ssq} - i={i} - y={y}')
                ssq.insert(0, sq)
            else:   
                if i==0:
                    ssq.append(sq)      
                for y in range(x, i):
                    print(f'sq={sq} : {ssq} - i={i} - y={y}')
                    if ssq[y] > sq:                    
                        ssq.insert(y, sq)
                        x = y
                        break
                    elif y == i-1:
                        x = y
                        ssq.append(sq)
    
            
        return ssq           
        
def main():
    nums = [0, 2, 5]
    # ssq = Solution()
    # print(ssq.sorted_squares(nums))
    ssq = Solution_second()
    print(ssq.sorted_squares(nums))
    
    
                 
if __name__ == "__main__":
    main()