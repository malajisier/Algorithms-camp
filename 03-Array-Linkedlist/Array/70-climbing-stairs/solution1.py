# 斐波那契数列问题
# n <= 2: 1, 2
# n >= 2: 那么第n个台阶只能从n-1台阶跨一步，或者是从n-2台阶跨两步
# 问题就可以泛化为： f(n) = f(n-1) + f(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n + 1):
            f3 = f1 + f2
            f1 = f2 
            f2 = f3
        return f3
