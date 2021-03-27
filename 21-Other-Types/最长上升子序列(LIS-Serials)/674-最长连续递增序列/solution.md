#### 法一：遍历

```java
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int n = nums.length;
        if (nums == null || n == 0) return 0;

        int res = 1, count = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) count++;
            // 小于等于都不符合条件，count重置为1
            else count = 1;
            res = count > res ? count : res;
        }
        return res;
    }
}
```



#### 法二：动态规划

```python
# dp[i]：表示在第i个元素，它这个位置 递增元素的个数
# dp = [1] * n：初始化，每个位置至少是一个序列
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or not nums: return 0

        res = 1
        dp = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                res = max(res,dp[i])

        return res
```

