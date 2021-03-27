# 题意说明：
# M：未挖出的地雷
# E：未挖出的方块
# B：已挖出的空白方块并且没有地雷相邻
# X：已挖出的地雷
# 数字：有多少地雷与这块已挖出的方块相邻

#简洁版的实现
class Solution:
    def updateBoard(self, board, click):
        self.board = board
        row = click[0]
        col = click[1]
        if self.board[row][col] == 'M':
            self.board[row][col] = 'X'
        elif self.board[row][col] == 'E':
            self.dfs(click)

        return self.board

    def dfs(self, click):
        mine = 0
        m = len(self.board)
        n = len(self.board[0])
        row = click[0]
        col = click[1]

        search = [-1, 0, 1]
        for i in search:
            for j in search:
                # 跳过自身
                if i == 0 and j == 0:
                    continue 
                # 四周的8个位置，是否有雷
                if 0 <= row + i < m and 0 <= col + j < n:
                    if self.board[row+i][col+j] == 'M':
                        mine += 1
        
        # 根据雷数，更新数值
        if mine > 0:
            self.board[row][col] = str(mine)
            return 
        elif mine == 0:
            self.board[row][col] = 'B'

        for i in search:
            for j in search:
                if 0 <= row + i < m and 0 <= col + j < n:
                    if self.board[row+i][col+j] == 'E':
                        # 下探
                        self.dfs([row+i, col+j])
        return


