# DP：使用二维数组，TC:O(m*n), SC:O(1)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m是行，n是列
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1: return 0

        obstacleGrid[0][0] = 1

        # 第一列填值，前面没有障碍物的置为1，障碍物置为0，障碍物之后置为0
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)
        # 第一行
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)
        
        # 当前位置有路径可走时，等于左侧+上方的路径之和
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    # 如果是障碍物，置为0，无路可走 
                    obstacleGrid[i][j] = 0
        
        return obstacleGrid[m - 1][n - 1]