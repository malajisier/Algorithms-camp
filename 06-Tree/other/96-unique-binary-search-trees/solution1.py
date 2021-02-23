# 思路：每个根i  都是由左子树（1, 2, ..., i - 1)和右子树（i + 1, i + 2, ..., n)组成的
#      每个根i 能组成的情况是两个子树情况的积，累加每个根的情况

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n] 