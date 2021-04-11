# 优化空间复杂度：使用滚动数组，只储存第i 个房子的前两间房
# TC:O(N), SC:O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        if n == 1: return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first + nums[i], second)
        
        return second




# 简洁版   
class Solution:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0

        for num in nums:
            cur, pre = max(pre + num, cur), cur

        return cur