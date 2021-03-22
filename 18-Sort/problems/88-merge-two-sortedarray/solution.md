题目：    
有序整数数组nums1,nums2, 两者初始化个数m,n     
把nums2合并到nums1，可认为合并后的nums1 空间大小为m+n 
- 归并的思想    

### 法一：双指针
- 简单直接
- TC:O(m+n), SC:O(m)
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted

```

三指针     
- 思路：从后往前，依次找最大的放在尾部
- TC: O(m+n), SC:O(1)       


```java
// 写法一：   
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int tail = m + n - 1;

        while (p1 >= 0 && p2 >= 0) {
            // if (nums1[p1] > nums2[p2]) {
            //     nums1[tail--] = nums1[p1--];
            // } else {
            //     nums1[tail--] == nums2[p2--];
            // }
            nums1[tail--] = nums1[p1] > nums2[p2] ? nums1[p1--] : nums2[p2--];
        }

        // nums2可能没遍历完结束
        for (int i = 0; i <= p2; i++) {
            nums1[i] = nums2[i];
        }
    }
}


// 写法二：
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1, p2 = n - 1;
        int p = m + n - 1;
        while (p2 >= 0) {
            if (p1 > 0 && nums1[p1] > nums[p2]) {
                nums1[p--] = nums1[p1--];
            } else {
                nums1[p--] = nums2[p2--];
            }
        }
    }
}
```