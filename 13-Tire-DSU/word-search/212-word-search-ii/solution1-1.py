# https://leetcode-cn.com/problems/word-search-ii/solution/pythonzi-dian-shu-dfs-by-mai-mai-mai-mai-zi/
# 简洁版的字典树+DFS

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node["#"] = True
        
        
        def search(i, j, node, pre, visited):
            if "#" in node:
                res.add(pre)
            
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i + di, j + dj
                if 0 <= x < rows and 0 <= y < cols and board[x][y] in node and (x, y) not in visited:
                    search(x, y, node[board[x][y]], pre + board[x][y], visited | {(x, y)})
        
        res, rows, cols = set(), len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)