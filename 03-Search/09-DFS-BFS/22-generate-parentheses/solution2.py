# 回溯法：只有在序列仍然保持有效时，才添加左右括号，通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点 


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s = '', left = 0, right = 0):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
            
        backtrack()
        return res