要求：

- 根据索引删除后，每一行都是按 **字典序**排列



思路

- 找到最长上升子序列
- 减去LIS的长度，就是 需要删除的元素索引 的最小值



#### 1、详细版本

```java
class Solution {
    public int minDeletionSize(String[] A) {
        int len = A[0].length();
        int[] dp = new int[len];
        Arrays.fill(dp, 1);

        for (int i = 0; i < len; i++) {
            for (int j = 0; j < i; j++) {
                boolean flag = false;
                // 求每一行的LIS
                for (String a : A) {
                    if (a.charAt(j) <= a.charAt(i)){ 
                        flag = true;
                    } else { 
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
		
        int longest = 0;
        for (int num : dp) {
            longest = Math.max(longest, num);
        }
        // 减去最长的LIS，就是需要
        return len - longest;
    }
}
```





#### 2、简洁版

```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A[0])
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                # all() 用于判断 给定的可迭代iterable里的所有元素，是否都为true
                if all(A[k][i] >= A[k][j] for k in range(len(A))):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return n - max(dp)
```

