# 问题描述：
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 


class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        if n == 2:
            return 2

        f1, f2, f3 = 1, 2, 3

        for i in range(3, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        
        return f3 % 1000000007