# 198.的进阶，房间是环状排列，意味着第一个和最后一个房子只能二选一，可约化成两个单排排列的子问题    
# TC:O(N), SC:O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        
        # 兼顾到特殊情况
        return max(helper(nums[1:]), helper(nums[:-1])) if len(nums) != 1 else nums[0]