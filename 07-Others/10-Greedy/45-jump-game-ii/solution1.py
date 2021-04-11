# 贪心解法：只在乎每一步能跳到的最远位置，TC:O(n)

class Solution:
    def jump(self, nums: List[int]) -> int:
        steps, maxpos, end = 0, 0, 0
        for i in range(len(nums) - 1):
            # 找能跳最远的
            maxpos = max(maxpos, i + nums[i])
            if i == end:
                maxpos = end
                steps += 1
        
        return steps