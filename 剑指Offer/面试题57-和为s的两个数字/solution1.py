# https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/solution/mian-shi-ti-57-he-wei-s-de-liang-ge-shu-zi-shuang-/

# 对撞双指针
# 时间复杂度：O(N)，空间复杂度:O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j  = 0, len(nums) - 1

        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return nums[i], nums[j]
        
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [nums[l], nums[r]]
            elif s > target:
                r -= 1
            else:
                l += 1
        
        return []
            