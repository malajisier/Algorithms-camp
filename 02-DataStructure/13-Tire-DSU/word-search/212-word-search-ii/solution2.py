# https://leetcode-cn.com/problems/word-search-ii/solution/dan-ci-sou-suo-ii-by-leetcode/
# 使用前缀树的回溯

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        END_WORD = "#"   
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[END_WORD] = END_WORD

        rows, cols = len(board), len(board[0])
        match = []


        def backtrack(i, j, parent):
            letter = board[i][j]
            cur_node = parent[letter]

            word_match = cur_node.pop(END_WORD, False)
            if word_match: match.append(word_match)         
            board[i][j] = "@"

            # 四联通图的遍历
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i + dx, j + dy
                if x < 0 or x >= rows or y < 0 or y >= cols: continue
                if not board[x][y] in cur_node: continue
                backtrack(x, y, cur_node)
            
            board[i][j] = letter
            if not cur_node: parent.pop(letter)
    
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie:
                    backtrack(row, col, trie)
        return match