# 暴力法 ：
# 最直接的方法：遍历每个滑动窗口，取最大值。共n-k+1个窗口
# TC:O(nk),n为数组元素个数  SC: O(n-k+1)
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        return [max(nums[i, i + k])for i in range(n - k + 1)]


# 第二种暴力解法：
# TC：(n-k+1)^2
# res = []
#         if nums != []:
#             for i in range(len(nums) - k + 1):
#                 cur_max = max(nums[i: i + k])
#                 res.append(cur_max)
#             return res