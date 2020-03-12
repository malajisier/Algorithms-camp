# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字

# 示例：
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3 

# 它考察的是程序员的沟通能力，先问面试官要时间/空间需求！！！
# 只是时间优先就用字典，
# 还有空间要求，就用指针+原地排序数组，
# 如果面试官要求空间O(1)并且不能修改原数组，还得写成二分法！！！   

# 若 nums[i] == i ： 说明此数字已在对应索引位置，无需交换，因此执行 i += 1 与 continue ；
# 若 nums[nums[i]] == nums[i] ： 说明索引 nums[i] 处的元素值也为 nums[i]，即找到一组相同值，返回此值 nums[i]；
# 否则： 当前数字是第一次遇到，因此交换索引为 i 和 nums[i] 的元素值，将此数字交换至对应索引位置。

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue

            if nums[nums[i]] == nums[i]:
                return nums[i]
            
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        
        return -1