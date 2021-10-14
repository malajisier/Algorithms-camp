```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;

        // 取到n+1位置
        int[] dp = new int[n + 1];

        // dp 数组：爬到第i层楼梯，有dp[i]中方法
        // 初始化，第一阶只有一种，第二阶有两种
        // dp[0]=1，没有意义忽略掉
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }
}
```       
- 时间复杂度：O(n)  
- 空间： O(n)     


```java
// 优化空间
class Solution {
    public int climbStairs(int n) {
        if (n <= 1) return 1;

        int[] dp = new int[3];
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i <= n; i++) {
            int tmp = dp[1] + dp[2];
            dp[1] = dp[2];
            dp[2] = tmp;
        }

        return dp[2]; 
    }
}
```    
- 时间复杂度：O(n)  
- 空间： O(1)        

    
*****************************      

进一步拓展：     
一步一个台阶，两个台阶，直到m个台阶，有多少种方法爬到n阶楼顶          

```java
class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (i - j >= 0) dp[i] += dp[i - j];
            }
        }
        return dp[n];
    }
}
```