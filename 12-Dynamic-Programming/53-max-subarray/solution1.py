# 动态规划的三种解法
# dp转移方程：dp[i] = max(nums[i], nums[i] + dp[i - 1])
# 最大子序和 = 当前元素最大 或者  包含之前和元素和最大


# 方法一：
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            # dp[i] = max(0, dp[i - 1]) + nums[i]

        return max(dp)


# 方法二：
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 直接在nums原数组上进行更改，时间复杂度更优
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        return max(nums)


# 方法三： 不需要新开数组，只用常量保存中间结果就可以
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, res = 0, nums[0]

        for num in nums:
            pre = max(pre, pre + num)
            res = max(res, pre)

        return res


# 远古写法：
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum = 0
        for i in range(len(nums)):
            if(sum + nums[i] > nums[i]):
                sum += nums[i]
            else:
                sum = nums[i]
            ans = max(ans, sum)
        return ans
