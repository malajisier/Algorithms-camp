```python
# 动态规划解法一：使用二维数组保存每个位置的状态 
# TC:O(mn), SC:O(mn)
# 注意：m是列, n是行  

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 将第一行和第一列置为1，根据列数构建行
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]


# 方法二：只保留当前层和前一层的状态
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]

        return cur[n - 1]
```