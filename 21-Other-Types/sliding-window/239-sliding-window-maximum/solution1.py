# https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/mian-shi-ti-59-i-hua-dong-chuang-kou-de-zui-da-1-6/

# deque：
# （1）仅包含窗口内元素
# （2）deque内元素非严格递减，新添加元素nums[j+1]时，必须删除所有 小于nums[j+1] 的元素


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        deque = collections.deque()

        # 滑动窗口未形成之前
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        
        res = [deque[0]]
        # 窗口形成之后
        for i in range(k, len(nums)):

            # i-k已在区间之外，当队列头部元素与num[i-k]相等时，说明头部元素已经不在区间了
            if deque[0] == nums[i - k]:
                deque.popleft()

            # 队尾元素小于nums[i]时，抛出队尾元素，并把nums[i]加入队列
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        
        return res
