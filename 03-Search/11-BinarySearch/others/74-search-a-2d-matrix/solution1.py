# 二分查找法，把n*m的数组转化成(0, n*m-1)的一维数组
# 行列转换:  行：idx//cols, 列：idx%cols
# TC:O(log(nm)), SC:O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0: return False
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1
        while l <= r:
            mid_idx = (l + r) // 2
            mid_val = matrix[mid_idx // cols][mid_idx % cols]
            
            if target == mid_val:
                return True
            else:
                if target < mid_val:
                    r = mid_idx - 1
                else:
                    l = mid_idx + 1
        
        return False


# class Solution:
#     def searchMatrix(self, matrix, target):
#         # 暴力法，TC:O(n*m),SC:O(1)
#         for row in matrix:
#             if target in row:
#                 return True
            
#         return False