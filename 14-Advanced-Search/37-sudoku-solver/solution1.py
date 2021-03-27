# 回溯

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 每个行、列、块 剩余的可用数字
        rows = [set(range(1, 10)) for _ in range(9)]
        cols = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]

        # 预先遍历一次，去除已用数字，挑出空闲格子
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    rows[i].remove(val)
                    cols[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))


        def backtrack(iter = 0):
            if iter == len(empty):
                return True
            
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3

            for val in rows[i] & cols[j] & block[b]:
                rows[i].remove(val)
                cols[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)

                if backtrack(iter + 1):
                    return True
                
                # 回溯失败，则恢复到上一层的状态
                rows[i].add(val)
                cols[j].add(val)
                block[b].add(val)
            
            return False
        
        backtrack()
