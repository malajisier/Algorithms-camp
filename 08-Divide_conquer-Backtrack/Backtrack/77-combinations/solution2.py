# 简洁版的回溯   

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first, pre = []):
            if len(pre) == k:
                res.append(pre[:])

            for i in range(first, n + 1):
                pre.append(i)
                backtrack(i + 1, pre)
                pre.pop()
        
        res = []
        backtrack()
        return res        