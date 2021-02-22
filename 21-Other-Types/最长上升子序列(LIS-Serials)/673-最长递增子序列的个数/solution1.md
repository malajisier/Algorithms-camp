#### 法一：动态规划

- 两个数组：
  - dp[] : 以nums[i] 结尾的 lis长度
  - counts[]: 以nums[i] 结尾的 lis 的组合数量

- TC:O(N^2),  SC: O(N)

题解：

https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/dong-tai-gui-hua-dong-tu-fu-zhu-li-jie-ru-you-bang/



```java
class Solution {
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length;
        if (n == 0 || nums == null) return 0;
		
        // dp[] 换为 length[]更贴切
        int[] dp = new int[n];
        int[] counts = new int[n];
        // 初始化为1，每个位置至少有一个LIS（自己本身）
        Arrays.fill(dp, 1);
        Arrays.fill(counts, 1);
        int longest = 0;
		
        // 两遍扫描
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                // 只有大于时，LIS才成立
                if (nums[i] > nums[j]) {
                    // 说明第一次找到 dp[i]和之前数字 组成的组合，
                    if (dp[j] + 1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                        
                        // 这里可以这么理解：以 j为结尾的每个组合，结尾再添加个nums[i]
                        counts[i] = counts[j];
                        
                    // 相等则 说明dp[i]的组合已经找到过一次了，    
                    } else if (dp[j] + 1 == dp[i]) {
                        counts[i] += counts[j];
                    }
                }
            }
            longest = Math.max(longest, dp[i]);
        }

        int total = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == longest) total += counts[i];
        }
        return total;
    }
}
```

