dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 
END_WORD = "#"

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        if not words: return[]
        # set为了判重
        self.res = set()

        # 构建Trie
        root = collections.defaultdict()
        for word in words:
            node = root
            for letter in word:
                node = node.setdefault(letter, collections.defaultdict())
            node[END_WORD] = END_WORD
        
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                # 剪枝，如果board里的字母，不在tire中所有的单词里，过滤掉
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)
        return list(self.res)

    
    def _dfs(self, board, i, j, cur_word, cur_dict):
        # 1.递归终止条件
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if END_WORD in cur_dict:
            self.res.add(cur_word)
        
        # 2.处理当前层逻辑
        # board[i][j]由tmp代存，并被其他字符暂替，防止重复使用
        tmp, board[i][j] = board[i][j], "@"
        # 四联通扩散 
        for k in range(4):
            x, y = i + dx[k], j + dy[k]

            # 3.下探到下一层，明确xy的范围，
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != "@" and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)

        # 4.回复当前层逻辑        
        board[i][j] = tmp