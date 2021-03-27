# 一次迭代： TC:O(1),  SC:O(1)
# keys：
# （1）枚举每个子数独
# （2）使用哈希映射（value-->count），确保每行、每列、每个子数独没有重复数字  

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 使用字典来存每行每列每个子数独
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                        return False

        return True