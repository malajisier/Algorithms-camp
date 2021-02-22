

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums or len(nums) == 0:
            return False
        l , r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True

            # 处理重复元素
            if nums[mid] == nums[l]:  # l和mid重复，l加一
                l += 1
            elif nums[mid] == nums[r]:  # mid和r重复，r减一
                r -= 1

            elif nums[mid] > nums[l]:  # l到mid是有序的，判断target是否在其中
                if nums[l] <= target < nums[mid]:  # target在其中，选择l到mid这段
                    r = mid - 1
                else:  # target不在其中，扔掉l到mid这段
                    l = mid + 1
            elif nums[mid] < nums[r]:  # mid到r是有序的，判断target是否在其中
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1 
        return False