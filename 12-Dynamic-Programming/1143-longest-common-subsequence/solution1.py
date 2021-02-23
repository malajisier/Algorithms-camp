# https://leetcode-cn.com/problems/longest-common-subsequence/solution/chao-xiang-xi-dong-tai-gui-hua-jie-fa-by-shi-wei-h/

# 求两个字符串的最长子序列
# 子问题划分：字符串s1, s2,
# （1）如果s1 的最后一位 等于 s2的最后一位，则两者的最大子序列就是 s1[0, i-1]和s2[0, i-1]两个字符串的最大子序列+1
# （2）如果两者最后一位不相等，最大子序列就是 
#          s1[0, i-1], s2[0, j]
#          s1[0, i], s2[0, j-1] 两个子序列的最大值

# 使用一个二维表格存储结果，子问题的具体实现：
    #   如果s1[i]==s2[j]，则dp[i][j]=dp[i-1][j-1]+1
    #   若不相等，dp[i][j]=max(dp[i-1][j],dp[i][j-1])


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]

        