# 回溯实现1

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1: return []

        self.res = []
        # 主对角线(左上右下)/dale diagonal：横纵坐标之差固定, i-j=0
        # 次对角线/hill diagonal：横纵坐标之和固定, i+j=n

        # 之前的皇后所能攻击到的位置
        self.cols, self.dale, self.hill = set(), set(), set()
        self.dfs(n, 0, [])
        return self.res2board(n)
    
    def dfs(self, n, row, cur):
        if row >= n:
            self.res.append(cur)
            return
        
        # 遍历所有的列
        for col in range(n):
            if col in self.cols or row - col in self.dale or row + col in self.hill:
                continue
            
            # 满足条件后，尝试将当前皇后放到cols，并更新cols
            self.cols.add(col)
            self.dale.add(row - col)
            self.hill.add(row + col)
            # 下探到下一层
            self.dfs(n, row + 1, cur + [col])

            # reverse state
            self.cols.remove(col)
            self.dale.remove(row - col)
            self.hill.remove(row + col)
    
    def res2board(self, n):
        board = []
        for res in self.res:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        
        return [board[i: i + n] for i in range(0, len(board), n)]