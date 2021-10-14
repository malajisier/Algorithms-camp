
```java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;

        // dp[i]定义: 到达第 i个台阶所花费的最少体力
        int[] dp = new int[n];

        dp[0] = cost[0];
        dp[1] = cost[1];

        for (int i = 2; i < n; i++) {
            dp[i] = Math.min(dp[i - 1], dp[i - 2]) + cost[i];
        }

        // 一次只能跳一两阶，直接在最后两位间取最小的
        return Math.min(dp[n - 1], dp[n - 2]);
    }
}
```    
- 时间复杂度：O(n)
- 空间复杂度：O(n)  

