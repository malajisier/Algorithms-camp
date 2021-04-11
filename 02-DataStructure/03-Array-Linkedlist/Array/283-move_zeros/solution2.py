class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方法二： “数0”，非零元素直接依次从头排列，记录次数，零直接在后面追加
        # TS: O(N+a), a为零的个数
        i = j = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
            else:
                pass

        for j in range(i, len(nums)):
            nums[j] = 0 

