# 题目描述：
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1. 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        f1, f2, fn = 0, 1, 0

        # for循环左闭右开
        for i in range(2, n + 1):
            fn = f1 + f2
            f1 = f2
            f2 = fn 

        return fn % 1000000007