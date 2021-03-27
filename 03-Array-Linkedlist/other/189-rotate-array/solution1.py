class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # k给定的范围是非负，所以很可能会大于数组的长度，此时就需要取余了
        # 切片
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + [:n - k]


        # 插入
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())


        # 暴力法，时间复杂度：O(n*k)
        # for i in range(k):
        #     last = nums[len(nums) - 1]
        #     for j in range(len(nums)):
        #         tmp = nums[j]
        #         nums[j] = last
        #         last = tmp