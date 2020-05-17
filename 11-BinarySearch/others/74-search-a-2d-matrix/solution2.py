# 双指针法（减治法）：因为矩阵有序，从右上角开始搜索，一行或一列不适合就删掉
# 如果 当前元素>target，往左走col-1，小于target，往下走row+1
# TC:O(n+m), SC:O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """ 
        if not matrix: return False

        n, m = len(matrix), len(matrix[0]) - 1
        row, col = 0, m

        while (row < n and col >= 0):
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True

        return False