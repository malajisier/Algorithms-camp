# 题目描述： 和154相同
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素，
# 数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers) - 1

        while l < r:
            mid = (l + r) // 2
            if numbers[mid] < numbers[r]:
                r = mid
            elif numbers[mid] > numbers[r]:
                l = mid + 1
            else:
                r -= 1

        return numbers[r]