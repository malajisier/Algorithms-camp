求最长上升子序列过程 的二维版本

- 要求：小信封的宽度和高度分别“严格”小于大信封的宽度和高度
- 思路：
  - 在宽度相等的时候，让高度不能出现“上升的子序列”，即首先按照宽度“升序排序”，在宽度相等的时候，按照高度“降序排序”
  - 最长上升子序列的算法特性，保证了宽度相等时，最多只能选一个



#### 方法一：贪心+二分

TC: O(nlogn)，遍历数组O(N), 二分O(logN)

SC: O(N)

```python
# 把 求最长上升子序列过程 提取成函数，推荐
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def lis(nums):
            res = []
            for i in range(len(nums)):
                h = nums[i][1]
                # 当前高度 大于height数组的最后一个，即当前高度 大于最大高度，直接添加
                if not res or h > res[-1]:
                    res.append(h)
                    l, r = 0, len(res) - 1
                    
                # 否则，在数组中寻找 第一个大于当前高度的元素，替换掉这个元素
                # 贪心思想：让子序列递增的速度 放缓
                else:
                    while l < r:
                        mid = (l + r) // 2
                        if res[mid] < h:
                            l = mid + 1
                        else:
                            r = mid
            		res[l] = h
           return len(res)
                  
        size = len(envelopes)
        if size < 2: return size
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        return lis(envelopes)
```



```python
# 基于过程的
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        size = len(envelopes)
        if size < 2: return size
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        height = [envelopes[0][1]]
        for i in range(1, size):
            h = envelopes[i][1]
            if h > height[-1]:
                height.append(h)
                continue
            
            l, r = 0, len(height) - 1
            while l < r:
                mid = (l + r) // 2;
                if height[mid] < h:
                    l = mid + 1
                else:
                    r = mid
            height[l] = h
        
        return len(height)
```



```java
/**
 * 另一种角度：https://leetcode-cn.com/problems/russian-doll-envelopes/solution/zui-chang-di-zeng-zi-xu-lie-kuo-zhan-dao-er-wei-er/
 */

class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        int n = envelopes.length;
        Arrays.sort(envelopes, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return a[0] == b[0] ? b[1] - a[1] : a[0] - b[0];
            }
        });

        int[] height = new int[n];
        for (int i = 0; i < n; i++) {
            height[i] = envelopes[i][1];
        }
        return lis(height);
    }

    public int lis(int[] nums) {
        int piles = 0, n = nums.length;
        int[] top = new int[n];
        for (int i = 0; i < n; i++) {
            int poker = nums[i];
            int left = 0, right = piles;
            while (left < right) {
                int mid = (left + right) / 2;
                if (top[mid] >= poker) right = mid;
                else left = mid + 1;
            }
            if (left == piles) piles++;
            top[left] = poker;
        }
        return piles;
    }
}
```



#### 方法二：贪心

```

```

