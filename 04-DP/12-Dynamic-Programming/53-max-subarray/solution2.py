# 分治法，最大子序要么在左半边，要么在右半边，或者穿过中间
# 时间复杂度退化成:O(nlogn)，SC:O(1)



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            max_right = self.maxSubArray(nums[len(nums)//2:len(nums)])
        
        maxl = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            maxl = max(maxl, tmp)

        maxr = nums[len(nums) // 2]
        tmp = 0
        for j in range(len(nums) // 2, len(nums)):
            tmp += nums[j]
            maxr = max(maxr, tmp)
        
        return max(max_left, max_right, maxl + maxr)
