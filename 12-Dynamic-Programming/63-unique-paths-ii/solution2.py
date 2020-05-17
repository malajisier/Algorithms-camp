# 一维数组的DP：优化数组空间，逐行计算当前最新路径条数，并覆盖上一行的路径条数

class Solution:
def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    # 初始化第一行，并多加一列，解决边界问题
    dp = [1] + [0] * n

    for i in range(0, m):
        for j in range(0, n):
            # dp[j]是上一行的d[j]，d[j-1]是当前行 当前元素的前一个元素，执行后dp会被覆盖就成为了当前行的dp
            dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]

    return dp[-2]

