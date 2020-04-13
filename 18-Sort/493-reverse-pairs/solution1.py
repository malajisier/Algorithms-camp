# mergesort，简洁的py版本1，推荐
# 两个py版本的merge，都借助了系统的sort，严格的TC：logn*nlogn

class Solution(object):
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(low, high):
            if low + 1 >= high:
                return 0
            
            mid = (low + high) // 2
            cnt = mergeSort(low, mid) + mergeSort(mid, high)

            j = mid
            for i in nums[low: mid]:
                while j < high and i > 2 * nums[j]:
                    j += 1
                cnt += j - mid

            nums[low: high] = sorted(nums[low: high])
            return cnt

        return mergeSort(0, len(nums))





