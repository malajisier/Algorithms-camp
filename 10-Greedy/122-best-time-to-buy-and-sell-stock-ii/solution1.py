# 贪心实现，最优方法使用动态规划解决

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit += (prices[i] - prices[i - 1])
        
        return maxProfit