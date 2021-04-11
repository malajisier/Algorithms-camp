# 回溯实现

class Solution:
    lookup = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

    def dfs(self, i, digits, res, tmp):
        if i == len(digits):
            res.append(''.join(tmp))
            return
        
        for s in self.lookup[digits[i]]:
            tmp.append(s)
            self.dfs(i + 1, digits, res, tmp)
            tmp.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
    
        res = []
        tmp = []
        self.dfs(0, digits, res, tmp)
        return res