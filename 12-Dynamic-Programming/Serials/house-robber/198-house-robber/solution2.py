# 思路和s2-java一样， dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
# TC:O(N)，SC:O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        # 同样，需要 n>=2
        if n == 1: return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        # 长度为n，取最后一个
        return dp[n - 1]


