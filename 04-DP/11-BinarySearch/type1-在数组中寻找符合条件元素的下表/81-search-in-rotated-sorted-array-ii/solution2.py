# 两种方法思路是一样的，两端元素与中间元素的对比

# 法一：右端元素 与中间元素进行对比
class Solution1:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums or len(nums) == 0:
            return False
        l , r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r- l) // 2

            if nums[mid] == target:
                return True

            # 右半序列是有序的
            elif nums[mid] < nums[r]:
                # 注意：mid、target 是严格大于，否则相等在上面已经直接返回true
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            # 左半序列是有序的
            elif nums[mid] > nums[r]:
                # 同理：mid、target 是严格小于
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1         
            # 条件：nums[mid]=nums[r]
            else:
                r -= 1
        
        return False



# 法二：左端元素 与中间元素对比
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums or len(nums) == 0:
            return False
        l , r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True
            elif nums[l] < nums[mid]:
                # 还是需要 严格大于的情况
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
        
        return False