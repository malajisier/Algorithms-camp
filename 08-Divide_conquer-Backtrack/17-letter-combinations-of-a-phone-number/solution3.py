# 简洁版递归

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def helper(level, visited):
            if level == n:
                res.append(visited)
                return 
            for s in lookup[digits[level]]:
                helper(level + 1,visited + s)


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

        n = len(digits)
        if not digits: return []
        
        res = []
        helper(0,"")
        return res