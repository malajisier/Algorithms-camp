#### 法一：双指针+贪心思想   
解读：   
- https://leetcode-cn.com/problems/increasing-triplet-subsequence/solution/shi-yong-shuang-zhi-zhen-qiu-jie-by-liu-fei-3/

最优时空：  
TC:O(N),  SC:O(1)    

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False

        small, mid = float('inf'), float('inf')
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            elif num > mid:
                return True
        
        return False

```