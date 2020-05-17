# 递归解法1：当行列过大时，会超时    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j):
            if i == 0 or j == 0:
                return 1
            return helper(i - 1, j) + helper(i, j - 1)
    
    return helper(m - 1, n - 1)


# 递归解法2：加入缓存数组，避免重复计算
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j):
            if i == 0 or j == 0:
                return 1
            
            if cache[j][i]: return cache[j][i]
            cache[j][i] = helper(i - 1, j) + helper(i, j - 1)
            return cache[j][i]
        
        cache = [[None for _ in range(n)] for _ in range(m)]
        return helper(m - 1, n - 1)
            