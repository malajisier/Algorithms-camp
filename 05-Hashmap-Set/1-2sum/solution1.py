class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力法，O(n^2)
        # n = len(nums)
        # for i, m in enumerate(nums):
        #     j = i + 1
        #     while j < n:
        #         if target == (m + nums[j]):
        #             return [i, j]
        #         else:
        #             j += 1

        # 2. 哈希字典
        dic = {}
        # 建立映射
        for idx, num in enumerate(nums):
            dic[num] = idx

        for i, num in enumerate(nums):
            # 题目描述中，假设每种输入只会对应一个答案
            j = dic.get(target - num)
            if j is not None and i != j:
                return [i, j]