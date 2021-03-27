# 贪心的另一种解法

class Solution:
    def jump(self, nums: List[int]) -> int:
        res, start, end = 0, 0, 1
        while end < len(nums):
            maxpos = 0
            for i in range(start, end):
                maxpos = max(maxpos, i + nums[i])           
            start = end
            end = maxpos + 1
            res += 1
        
        return res