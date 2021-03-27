# 自底向上的动态规划

# class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     f = [0] * (len(triangle) + 1)

    #     for row in triangle[::-1]:
    #         for i in range(len(row)):
    #             f[i] = row[i] + min(f[i], f[i + 1])
        
    #     return f[0]




# 优化时间开销
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 直接使用triangle初始化dp，减少累加过程中频繁访问triangle的时间开销
        dp = triangle

        # 从倒数第二行开始向上累加，因为倒数第一行已经初始化了
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # 当前元素的最小路径，累加需要，下一行相邻元素的较小者
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
         
        return dp[0][0]