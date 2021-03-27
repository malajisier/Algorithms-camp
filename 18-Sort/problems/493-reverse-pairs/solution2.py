class Solution(object):
    def reversePairs(self, nums: List[int]) -> int:
        self.res = 0
        self.mergeSort(nums)
        return self.res

    def mergeSort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        
        mid = n // 2
        return self.merge(self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:]))

    def merge(self, left, right):
        l, r = len(left), len(right)
        i, j = 0, 0

        while i < l and j < r:
            if left[i] > 2 * right[j]:
                self.res += l - i
                j += 1
            else:
                i += 1
        return sorted(left + right)