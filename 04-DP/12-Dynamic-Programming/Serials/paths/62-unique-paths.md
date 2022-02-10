### 法一：dp    
```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }
}
```  

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


# 优化：一维数组保存，只保留当前层和前一层的状态
# 时间:O(mn), 空间: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]

        return cur[n - 1]
```  

### 法二：记忆化递归   
- 纯递归会有大量的重复调用导致超时，加个缓存  
```java
class Solution {
    public int uniquePaths(int m, int n) {
        return dfs(new HashMap<Pair,Integer>(), 0, 0, m, n);
    }

    private int dfs(Map<Pair,Integer> cache, int i, int j, int m, int n) {
        Pair p = new Pair(i,j);
        // (i,j) 如果在缓存中，直接返回
        if(cache.containsKey(p)) {
            return cache.get(p);
        }
        // 递归终止条件：到达边界
        if(i == m - 1 || j == n - 1) {
            return 1;
        }
        
        // map((i,j), 路径数)，继续递归，往下i+1, 往右j+1
        cache.put(p, dfs(cache, i + 1, j, m, n) + dfs(cache, i, j + 1, m, n) );
        return cache.get(p);
    }
}
```
