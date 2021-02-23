```python
# 贪心+二分
# 贪心：为了使上升子序列尽可能的长，则需要让序列上升得尽可能慢，所以要使子序列末尾的那个数尽可能小
# TC:O(nlogn),nums长度为n，二分过程logn

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        for num in nums:
            if not res or num > res[-1]:
                res.append(num)

            # 在res里查找，找到第一个小于num的数 res[k]，插到其后面res[k+1]=num
            else:
                l, r = 0, len(res) - 1
                loc = r
                while l <= r:
                    mid = l + (r - l) // 2
                    if res[mid] >= num:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1

                # 最后一位之前没有合适的插入位置，直接用num替换掉最后一位
                res[loc] = num
        
        return len(res)
```


```python
# 动态规划
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)                   
```

