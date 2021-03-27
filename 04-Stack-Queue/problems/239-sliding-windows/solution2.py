# 方法二：双向队列，在两端以常数时间压入/弹出元素
# 流程：
# - 处理前k个元素，初始化队列
# - 遍历整个数组，在每一步
#     - 只保留当前滑动窗口有的元素的索引  
#     - 移除比当前元素小的所有元素，因为它们肯定不是最大的
# - 将当前元素添加到双向队列中
# - 将deque[0]添加到输出，最后返回输出数组

# 时间复杂度：O(N)，每个元素被处理两次- 其索引被添加到双向队列中和被双向队列删除。
# 空间复杂度：O(N)，输出数组使用了O(N−k+1) 空间，双向队列使用了O(k)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        # case base
        if not nums:
            return []

        # 队列只存放索引值
        deq = deque()
        result = []

        for i in range(len(nums)):
            # 左边界出滑动窗,只有1种情况需要考虑，左边界是上轮循环的滑动窗口的最大值
            # 当元素从左边界滑出时，如果它恰好是滑动窗口的最大值，则将其弹出
            if i >= k and i - k == deq[0]:
                deq.popleft()

            # 当前值大于等于滑动窗口元素时，将元素弹出
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            # 队首一定是滑动窗口的最大值的索引
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result


# 另一种写法
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         deq = collections.deque()
#         res = []

#         for i, num in enumerate(nums):
#             while deq and deq[0] <= i - k: deq.popleft()
#             while deq and num > nums[deq[-1]]: deq.pop()
#             deq.append(i)

#             if i >= k - 1:
#                 res.append(nums[deq[0]])
#         return res
       